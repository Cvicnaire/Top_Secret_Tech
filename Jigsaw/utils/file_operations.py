def read_task(task_filename):
    with open(task_filename, 'r') as file:
        return file.read()

def read_variables(variable_file):
    variables = {}
    with open(variable_file, 'r') as file:
        for line in file:
            key, value = line.strip().split('=', 1)
            variables[key] = value
    return variables

