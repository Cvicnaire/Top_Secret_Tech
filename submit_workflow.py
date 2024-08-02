import os
import subprocess
from glob import glob

def get_most_recent_file(directory, pattern):
    files = glob(os.path.join(directory, pattern))
    if not files:
        return None
    files.sort(key=lambda x: os.path.getmtime(x), reverse=True)
    return files[0]

def submit_to_cromwell(json_dir, workflow_dir):
    most_recent_json = get_most_recent_file(json_dir, 'inputs_*.json')
    most_recent_workflow = get_most_recent_file(workflow_dir, 'composed_workflow_*.wdl')
    
    if not most_recent_json or not most_recent_workflow:
        print("No recent input JSON or composed workflow files found.")
        return
    
    print(f"Submitting {most_recent_json} and {most_recent_workflow} to Cromwell.")
    
    try:
        result = subprocess.run(['/projectnb/bubhub/cromwell/cromwell_run.sh', '-i', most_recent_json, most_recent_workflow],
                                check=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error during submission: {e}")
        print(f"Return code: {e.returncode}")
        print(f"Output: {e.output}")
        print(f"StdErr: {e.stderr}")

json_dir = "json_inputs"
workflow_dir = "workflows"

submit_to_cromwell(json_dir, workflow_dir)
