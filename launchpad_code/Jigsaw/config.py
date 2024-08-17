"""config.py: Configuration file for Jigsaw"""
import os

workflow_template_file = "workflow_template.wdl"
variables_file = "variables.py"
workflow_output_dir = "composed_workflows"
json_output_dir = "json_inputs"

# Ensure the directories exist
os.makedirs(workflow_output_dir, exist_ok=True)
os.makedirs(json_output_dir, exist_ok=True)
