"""
Module to generate unique IDs for each workflow run.
"""

def get_next_unique_id(id_file="last_id.txt"):
    """Function to generate a unique ID for each workflow run."""
    try:
        with open(id_file, 'r', encoding="utf-8") as file:
            content = file.read().strip()
            last_id = int(content) if content else 0
    except FileNotFoundError:
        last_id = 0
    next_id = last_id + 1
    with open(id_file, 'w', encoding="utf-8") as file:
        file.write(f"{next_id:06d}")
    return f"{next_id:06d}"

if __name__ == "__main__":
    unique_id = get_next_unique_id()
    print(f"Generated Unique ID: {unique_id}")
