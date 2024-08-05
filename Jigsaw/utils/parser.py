"""Module to parse task files and assemble a workflow."""

import re
import json
import shutil
import os
from utils.file_operations import read_task
from utils.id_generator import get_next_unique_id
from utils.submission import submit_workflow

def extract_task_io(task_content):
    """Function to extract task inputs and outputs."""
    inputs = re.findall(r"input {([\s\S]*?)}", task_content)
    outputs = re.findall(r"output {([\s\S]*?)}", task_content)
    return inputs, outputs


def extract_task_name(task_content):
    """Function to extract task name."""
    name = re.findall(r"task (\w+)", task_content)
    return name[0] if name else "UnknownTask"



def parse_task_inputs(inputs):
    """Function to parse task inputs."""
    task_inputs = {}
    for input_block in inputs:
        for line in input_block.splitlines():
            if line.strip():
                input_type, input_name = re.findall(r"(\w+)\s+(\w+)", line.strip())[0]
                task_inputs[input_name] = None  # Default value for optional inputs
    return task_inputs

"""Function to assemble the workflow."""
def assemble_workflow(variables, workflow_template_file, workflow_output_dir, json_output_dir):
    task_files = variables['task_files'].split(',')
    fastqc_flags = variables.get('fastqc_flags', "")
    outdirPath = variables.get('outdirPath', ".")

    task_definitions = ""
    workflow_inputs = ""
    workflow_outputs = ""
    task_calls = ""
    all_inputs = {}

    for task_file in task_files:
        task_content = read_task(task_file)
   
        if "task FastQC" in task_content:
            task_content = task_content.replace("${fastqc_flags}", fastqc_flags)
        # where i can add other flags from other packages if needed.
        task_definitions += task_content + "\n\n"
   
        inputs, outputs = extract_task_io(task_content)
        task_name = extract_task_name(task_content)
   
        task_inputs = parse_task_inputs(inputs)
  
        workflow_inputs += generate_workflow_inputs(task_inputs)
        workflow_outputs += generate_workflow_outputs(outputs, task_name)
        task_calls += generate_task_calls(task_inputs, variables, task_name)
        all_inputs.update({f"{task_name}.{key}": value for key, value in task_inputs.items()})

    workflow_template = read_workflow_template(workflow_template_file)
    composed_workflow = replace_placeholders(workflow_template, task_definitions, workflow_inputs, workflow_outputs, task_calls)

    unique_id = get_next_unique_id()
    output_workflow_file = f"composed_workflow_{unique_id}.wdl"
    json_output_file = f"inputs_{unique_id}.json"

    write_composed_workflow(composed_workflow, output_workflow_file)
    write_inputs_json(all_inputs, json_output_file)

    move_files(output_workflow_file, workflow_output_dir)
    move_files(json_output_file, json_output_dir)

    print(f"Workflow assembled and written to {os.path.join(workflow_output_dir, output_workflow_file)}")
    print(f"Inputs JSON written to {os.path.join(json_output_dir, json_output_file)}")

    submit_workflow()

def generate_workflow_inputs(task_inputs):
    workflow_inputs = ""
    for input_name in task_inputs.keys():
        workflow_inputs += f"    {input_name}? {input_name}\n"
    return workflow_inputs

def generate_workflow_outputs(outputs, task_name):
    workflow_outputs = ""
    for output_block in outputs:
        for line in output_block.splitlines():
            if line.strip():
                output_type, output_name = re.findall(r"(\w+)\s+(\w+)", line.strip())[0]
                workflow_outputs += f"    {output_type}? {output_name} = {task_name}.{output_name}\n"
    return workflow_outputs

def generate_task_calls(task_inputs, variables, task_name):
    task_calls = f"    call {task_name} {{\n"
    for input_name in task_inputs.keys():
        if input_name in variables:
            task_calls += f"        {input_name} = \"{variables[input_name]}\"\n"
        else:
            task_calls += f"        {input_name} = {input_name}\n"
    task_calls += "    }\n"
    return task_calls

def read_workflow_template(workflow_template_file):
    with open(workflow_template_file, 'r', encoding="utf-8") as template_file:
        workflow_template = template_file.read()
    return workflow_template

def replace_placeholders(workflow_template, task_definitions, workflow_inputs, workflow_outputs, task_calls):
    composed_workflow = workflow_template.replace("${task_definitions}", task_definitions.strip())
    composed_workflow = composed_workflow.replace("${workflow_inputs}", workflow_inputs.strip())
    composed_workflow = composed_workflow.replace("${workflow_outputs}", workflow_outputs.strip())
    composed_workflow = composed_workflow.replace("${task_calls}", task_calls.strip())
    return composed_workflow

def write_composed_workflow(composed_workflow, output_workflow_file):
    with open(output_workflow_file, 'w', encoding="utf-8") as output_file:
        output_file.write(composed_workflow)

def write_inputs_json(all_inputs, json_output_file):
    with open(json_output_file, 'w', encoding="utf-8") as json_file:
        json.dump(all_inputs, json_file, indent=4)

def move_files(file, output_dir):
    shutil.move(file, os.path.join(output_dir, file))
