import os
import re

folder_path = os.path.dirname(os.path.abspath(__file__))

for filename in os.listdir(folder_path):
    match = re.match(r'^task(\d)\.py$', filename)
    if match:
        digit = match.group(1)
        new_name = f'task0{digit}.py' 

        old_file = os.path.join(folder_path, filename)
        new_file = os.path.join(folder_path, new_name)

        os.rename(old_file, new_file)
        print(f'Переименовано: {filename} -> {new_name}')