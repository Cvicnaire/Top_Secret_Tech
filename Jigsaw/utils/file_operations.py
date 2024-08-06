"""Module for file operations"""
def read_task(task_filename):
    """Function to read the task file."""
    with open(task_filename, 'r', encoding = "utf-8") as file:
        return file.read()
