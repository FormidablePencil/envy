import os
import sys

# Get the target from command line arguments
target = sys.argv[1]

# Check if it is a file or a directory
if os.path.isfile(target):
    print(f"{target} is a file.")
elif os.path.isdir(target):
    print(f"{target} is a directory.")
else:
    print(f"{target} does not exist.")