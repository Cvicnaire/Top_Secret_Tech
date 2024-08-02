def get_next_unique_id(id_file="last_id.txt"):
    try:
        with open(id_file, 'r') as file:
            last_id = int(file.read().strip())
    except FileNotFoundError:
        last_id = 0
    
    next_id = last_id + 1
    with open(id_file, 'w') as file:
        file.write(f"{next_id:06d}")
    
    return f"{next_id:06d}"

