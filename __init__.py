#import sys
#sys.path.append("hellow")
#from helloworlddep import run
#run()
import os

def create_files(outer_dir, inner_dir1, inner_dir2):
    """
    Creates the specified directory structure with empty files.

    Args:
        outer_dir (str): The name of the outer directory.
        inner_dir1 (str): The name of the first inner directory.
        inner_dir2 (str): The name of the second inner directory.
    """

    # Create the outer directory
    os.makedirs(outer_dir, exist_ok=True)

    # Create the inner directories
    os.makedirs(os.path.join(outer_dir, inner_dir1), exist_ok=True)
    os.makedirs(os.path.join(outer_dir, inner_dir2), exist_ok=True)

    # Create the empty files
    with open(os.path.join(outer_dir, inner_dir1, "util_file.py"), "w") as f:
        pass
    with open(os.path.join(outer_dir, inner_dir2, "file_that_needs_function.py"), "w") as f:
        pass

# Example usage:
outer_dir = "Outer_dir"
inner_dir1 = "inner_dir1"
inner_dir2 = "inner_dir2"

create_files(outer_dir, inner_dir1, inner_dir2)