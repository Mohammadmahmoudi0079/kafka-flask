import json
import os

def fix_json_format(file_name, output_file_name):
    fixed_data = []

    # Read the improperly formatted JSON file
    with open(file_name, 'r') as file:
        for line in file:
            if line.strip():  # Skip empty lines
                try:
                    json_object = json.loads(line)
                    fixed_data.append(json_object)
                except json.JSONDecodeError as e:
                    print(f"Error decoding JSON: {e} in line: {line}")
    
    # Save the fixed data to a new file in proper JSON array format
    with open(output_file_name, 'a') as file:
        json.dump(fixed_data, file, indent=4)

    # Delete the original improperly formatted file
    os.remove(file_name)

