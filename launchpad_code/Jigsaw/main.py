import sys
import os
from utils.parser import assemble_workflow
import variables  # Import variables directly
from config import workflow_template_file, workflow_output_dir, json_output_dir

if __name__ == "__main__":
    # Ensure that variables from variables.py are used
    assemble_workflow(variables, workflow_template_file, workflow_output_dir, json_output_dir)
