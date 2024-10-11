import os
import sys
import subprocess
import argparse
import logging
from .test_runner import run_tests, run_all_tests_in_cwd
from .task_executor import execute_task
from .code_generator import generate_code_from_anywhere, apply_changes_from_anywhere
from utils.utils import is_empty
from cli_args import set_cli_args

def set_pythonpath(path):
    """Sets the PYTHONPATH environment variable."""
    if path:
        os.chdir(path)
        logging.info(f"PYTHONPATH set to: {path}")
    else:
        os.chdir(os.environ.get("py_PYTHONPATH", "envy"))
        logging.info(f"PYTHONPATH set to default: envy")

def main():
    args = set_cli_args(argparse)
    # pythonpath = args.pythonpath
    # set_pythonpath(pythonpath)
    # TODO: may just not need set_pythonpath since we are executing py as module rather than file

    if args.test or args.unit_test or args.integration_test:
        # Run tests
        if args.target:
            if args.unit_test:
                run_tests(args.target, 'unit')
            elif args.integration_test:
                run_tests(args.target, 'integration')
        elif not args.target or os.path.isdir(args.target): # TODO This code path is crusial to document
            run_all_tests_in_cwd(args)
    elif args.execute_task:
        # Execute a task
        task = {
            # Define the task details here
        }
        execute_task(task)
    elif args.generate_from_anywhere:
        # Generate code from anywhere
        task = {
            # Define the task details here
        }
        file_path = generate_code_from_anywhere(task)
        print(f"Generated code written to: {file_path}")
    elif args.apply_changes_from_anywhere:
        # Apply changes from anywhere
        file_path = args.target
        apply_changes_from_anywhere(file_path)
    else:
        # Run as a regular Python script
        if os.path.isfile(args.target):
            try:
                result = subprocess.run([sys.executable, args.target], check=True, capture_output=True, text=True)
                logging.info(f"Successfully executed command: {sys.executable} {args.target}")
                print(result.stdout)
            except subprocess.CalledProcessError as e:
                logging.error(f"Error running script: {e}")
                logging.error(f"Command output: {e.output}")
                logging.error(f"Command error: {e.stderr}")
                print(e)
                print(f"Error: The specified target '{args.target}' does not contain any executable code.")
                sys.exit(1)
        elif os.path.isdir(args.target):
            os.chdir(args.target)
            command = [sys.executable, "-m", "pytest", "--color=yes", "."]
            try:
                result = subprocess.run(command, check=True, capture_output=True, text=True)
                logging.info(f"Successfully executed command: {' '.join(command)}")
                print(result.stdout)
            except subprocess.CalledProcessError as e:
                logging.error(f"Error running command: {e}")
                logging.error(f"Command output: {e.output}")
                logging.error(f"Command error: {e.stderr}")
                print(f"Error: The specified target '{args.target}' does not contain any executable code.")
                sys.exit(1)
        else:
            logging.error(f"Error: The specified target '{args.target}' does not exist.")
            print(f"Error: The specified target '{args.target}' does not exist.")
            sys.exit(1)

if __name__ == "__main__":
    main()
