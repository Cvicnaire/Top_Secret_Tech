"""main module to run the workflow assembly"""

from utils.parser import assemble_workflow
from utils.file_operations import read_variables
from config import workflow_template_file, variables_file, workflow_output_dir, json_output_dir
if __name__ == "__main__":
    variables = read_variables(variables_file)
    assemble_workflow(variables, workflow_template_file, workflow_output_dir, json_output_dir)