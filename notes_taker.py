import sys
import os
from datetime import datetime

if len(sys.argv) < 2:
    print("Usage: python notes_taker.py <filename>")
    sys.exit()

else: # file path is provided
    if os.path.exists(sys.argv[1]): # check if file exists
        file_path = sys.argv[1]
        with open(file_path, "a") as file:
            # open file in append mode
            new_notes = True
            while new_notes:
                note = input("Enter your note: ")
                now = datetime.now()
                current_time = now.strftime("%Y-%m-%d %H:%M:%S")
                file.write(f"[{current_time}] {note}\n")

                if note == "exit":
                    new_notes = False

    else:
        print(f"File {sys.argv[1]} does not exist.")
        sys.exit()