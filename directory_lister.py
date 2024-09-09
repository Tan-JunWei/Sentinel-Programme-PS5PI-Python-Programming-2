# > python directory_lister.py /path/to/directory
# Contents of /path/to/directory: file1.txt
# file2.jpg
# subdirectory

# > python directory_lister.py Contents of current directory: script.py
# another_directory C:\Users\Admin\Desktop\CS\Quartz\quartz

import sys
import os

if len(sys.argv) < 2:
    # if directory path is not provided, list contents of current directory
    print("Contents of current directory:")
    current_dir = os.getcwd()
    for item in os.listdir(current_dir):
        print(item)

else:
    # if directory path is provided, list contents of that directory
    dir_path = sys.argv[1]

    if os.path.exists(dir_path):
        # check if directory exists
        print(f"Contents of {dir_path}:")
        for item in os.listdir(dir_path):
            print(item)
    else:
        print(f"Error: The directory '{dir_path}' does not exist.")
