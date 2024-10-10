import sys
import os
import subprocess
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from py_cmd.cli import main as cli_main

if __name__ == "__main__":
    cli_main()

    target = sys.argv[1]
    
    # try:
    #     result = subprocess.run(["pytest", sys.argv[1]], check=True, capture_output=True, text=True)
    #     print(result.stdout)
    #     print(result.stderr)
    #     print("kk")
    # except subprocess.CalledProcessError as e:
    #     # Print the error message from the CalledProcessError
    #     print(f"Error: {e.stderr}")
    #     print("kk2")
    # except Exception as e:
    #     print(e)
    #     print("kk")
    
    if os.path.isfile(target):
        print(f"{target} is a file.")
    elif os.path.isdir(target):
        print(f"{target} is a directory.")
    else:
        print(f"{target} does not exist.")
