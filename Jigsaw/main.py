from config import workflow_template_file, variables_file, workflow_output_dir, json_output_dir
from utils.file_operations.py import read_variables
from utils.parser import assemble_workflow

if __name__ == "__main__":
    variables = read_variables(variables_file)
    assemble_workflow(variables, workflow_template_file, workflow_output_dir, json_output_dir)