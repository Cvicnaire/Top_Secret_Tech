"""main module to run the workflow assembly"""
import sys
import os
from utils.parser import assemble_workflow
from utils.file_operations import read_variables
from config import workflow_template_file, variables_file, workflow_output_dir, json_output_dir
# Add the path to the 'utils' module to the Python module search path
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/utils')

if __name__ == "__main__":
    variables = read_variables(variables_file)
    assemble_workflow(variables, workflow_template_file, workflow_output_dir, json_output_dir)
