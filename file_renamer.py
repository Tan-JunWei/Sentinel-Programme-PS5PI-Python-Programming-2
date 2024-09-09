import sys
import os 

# Usage
# > python file_renamer.py C:\temp\oldname.txt
# newname.txt
# File renamed successfully: C:\temp\oldname.txt ->
# C:\temp\newname.txt

import sys
import os

# Ensure correct number of arguments are provided
if len(sys.argv) < 3:
    print("Usage: python file_renamer.py <old_file_path> <new_file_name>")
    sys.exit(1)

old_file_path = sys.argv[1]
new_file_name = sys.argv[2]

if os.path.exists(old_file_path):
    directory = os.path.dirname(old_file_path)
    new_file_path = os.path.join(directory, new_file_name)
    
    try:
        os.rename(old_file_path, new_file_path)
        print(f"File renamed successfully: {old_file_path} -> {new_file_path}")
    except OSError as e:
        print(f"Error renaming file: {e}")
else:
    print(f"Error: The file '{old_file_path}' does not exist.")
    sys.exit(1)

