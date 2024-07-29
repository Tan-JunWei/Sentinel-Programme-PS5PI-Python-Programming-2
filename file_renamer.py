import sys
import os 

if os.path.exists(sys.argv[1]):
    path = sys.argv[1]
    for file in os.listdir(path):
        if file.endswith(sys.argv[2]):
            os.rename(f"{path}/{file}", f"{path}/{file.replace(sys.argv[2], sys.argv[3])}")
