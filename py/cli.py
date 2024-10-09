import os
import sys
import subprocess
import argparse
import logging
from test_runner import run_tests, run_all_tests
from task_executor import execute_task
from code_generator import generate_code_from_anywhere, apply_changes_from_anywhere
from utils import set_pythonpath

def main():
    parser = argparse.ArgumentParser(description='Run a Python script, test suite, or AI-powered codebase operations.')
    parser.add_argument('target', nargs='?', default=None, help='The Python script, directory of tests, or task to execute.')
    parser.add_argument('-p', '--pythonpath', default=None, help='The PYTHONPATH to set.')
    parser.add_argument('-t', '--test', action='store_true', help='Run all tests (unit and integration).')
    parser.add_argument('-ut', '--unit-test', action='store_true', help='Run unit tests only.')
    parser.add_argument('-it', '--integration-test', action='store_true', help='Run integration tests only.')
    parser.add_argument('-e', '--execute-task', action='store_true', help='Execute a task using the CentralAIManager.')
    parser.add_argument('-g', '--generate-from-anywhere', action='store_true', help='Generate code from anywhere using the CentralAIManager.')
    parser.add_argument('-a', '--apply-changes-from-anywhere', action='store_true', help='Apply changes from anywhere using the CentralAIManager.')
    args = parser.parse_args()

    pythonpath = args.pythonpath
    set_pythonpath(pythonpath)

    if args.test or args.unit_test or args.integration_test:
        # Run tests
        if args.unit_test:
            run_tests(args.target, 'unit')
        elif args.integration_test:
            run_tests(args.target, 'integration')
        else:
            run_all_tests()
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