"""Module for file operations"""
def read_task(task_filename):
    """Function to read the task file."""
    with open(task_filename, 'r', encoding = "utf-8") as file:
        return file.read()

def read_variables(variable_file):
    """Function to read the variables file."""
    variables = {}
    with open(variable_file, 'r', encoding = "utf-8") as file:
        for line in file:
            key, value = line.strip().split('=', 1)
            variables[key] = value
    return variables
