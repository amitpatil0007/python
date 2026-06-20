import os

# Use the current folder
directory_path = r"D:\python.py\ch1.py\ps1.py"

# Get the list of files and directories
contents = os.listdir(directory_path)

print(f"Contents of '{directory_path}':")
for item in contents:
    print(item)