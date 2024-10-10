import os
import sys
import subprocess
import logging
from tests.test_mapping import TEST_MAPPING
import posixpath

def run_tests(target_path, test_type):
    """Runs the specified test type for the given target."""
    print(f"run_tests called with target_path: {target_path}")
    if os.path.isfile(target_path) and not target_path.startswith('test_'):
        # Find the corresponding test file(s) for the target file
        test_files = TEST_MAPPING.get(target_path, [])
        for test_file in test_files:
            if test_type == 'integration':
                test_dir = os.path.join(os.path.dirname(test_file), os.path.dirname(test_file))
                logging.info(f"Running integration tests for {target_path} in directory: {test_dir}")
                test_pattern = os.path.basename(test_file)
                # Run the tests
                command = ["pytest", "--color=yes", test_dir, "-k", test_pattern]
                try:
                    result = subprocess.run(command, check=True, capture_output=True, text=True)
                    logging.info(f"Successfully executed command: {' '.join(command)}")
                    print(result.stdout)
                except subprocess.CalledProcessError as e:
                    logging.error(f"Error running command: {e}")
                    logging.error(f"Command output: {e.output}")
                    logging.error(f"Command error: {e.stderr}")
                    print(f"Error running command: {e}")
                    print(f"Command output: {e.output}")
                    print(f"Command error: {e.stderr}")
                    sys.exit(1)
            elif test_type == 'unit':
                test_dir = os.path.join(os.path.dirname(test_file), os.path.dirname(test_file))
                logging.info(f"Running unit tests for {target_path} in directory: {test_dir}")
                test_pattern = os.path.basename(test_file)
                # Run the tests
                command = ["pytest", "--color=yes", test_dir, "-k", test_pattern]
                try:
                    result = subprocess.run(command, check=True, capture_output=True, text=True)
                    logging.info(f"Successfully executed command: {' '.join(command)}")
                    print(result.stdout)
                except subprocess.CalledProcessError as e:
                    logging.error(f"Error running command: {e}")
                    logging.error(f"Command output: {e.output}")
                    logging.error(f"Command error: {e.stderr}")
                    print(f"Error running command: {e}")
                    print(f"Command output: {e.output}")
                    print(f"Command error: {e.stderr}")
                    sys.exit(1)
            else:
                raise ValueError(f"Invalid test type: {test_type}")
    elif os.path.isfile(target_path) and target_path.startswith('test_'):
        # Run the specific test file
        test_dir = os.path.dirname(target_path)
        test_pattern = os.path.basename(target_path)
        # Run the tests
        command = ["pytest", "--color=yes", test_dir, "-k", test_pattern]
        try:
            result = subprocess.run(command, check=True, capture_output=True, text=True)
            logging.info(f"Successfully executed command: {' '.join(command)}")
            print(result.stdout)
        except subprocess.CalledProcessError as e:
            logging.error(f"Error running command: {e}")
            logging.error(f"Command output: {e.output}")
            logging.error(f"Command error: {e.stderr}")
            print(f"Error running command: {e}")
            print(f"Command output: {e.output}")
            print(f"Command error: {e.stderr}")
            sys.exit(1)
    elif os.path.isdir(target_path):
        print(f"run_tests called with directory target_path: {target_path}")
        if target_path == os.path.join(os.getcwd(), 'py'):
            # Run all tests in the py/tests directory
            unit_test_dir = os.path.join(target_path, 'tests', 'unit')
            integration_test_dir = os.path.join(target_path, 'tests', 'integration')
        else:
            # Run all tests in the envy/ directory
            unit_test_dir = os.path.join(os.getcwd(), 'tests', 'unit')
            integration_test_dir = os.path.join(os.getcwd(), 'tests', 'integration')

        if test_type == 'unit':
            command = ["pytest", "--color=yes", unit_test_dir]
            logging.info(f"Running unit tests in directory: {unit_test_dir}")
        elif test_type == 'integration':
            command = ["pytest", "--color=yes", integration_test_dir]
            logging.info(f"Running integration tests in directory: {integration_test_dir}")
        else:
            command = ["pytest", "--color=yes", unit_test_dir, integration_test_dir]
            logging.info(f"Running all tests in directories: {unit_test_dir}, {integration_test_dir}")

        try:
            result = subprocess.run(command, check=True, capture_output=True, text=True)
            logging.info(f"Successfully executed command: {' '.join(command)}")
            print(result.stdout)
        except subprocess.CalledProcessError as e:
            logging.error(f"Error running tests: {e}")
            logging.error(f"Command output: {e.output}")
            logging.error(f"Command error: {e.stderr}")
            print(f"Error running tests: {e}")
            print(f"Command output: {e.output}")
            print(f"Command error: {e.stderr}")
            sys.exit(1)
    else:
        logging.error(f"Error: The specified target '{target_path}' is not a valid file or directory.")
        print(f"Error: The specified target '{target_path}' is not a valid file or directory.")
        sys.exit(1)

def run_all_tests(target_path):
    """Runs all tests (unit and integration) in the 'envy' directory."""
    print("run_all_tests called")
    target_dir = posixpath.basename(posixpath.dirname(target_path))
    print(target_dir)
    unit_test_dir = os.path.join(target_dir, 'tests', 'unit')
    integration_test_dir = os.path.join(target_dir, 'tests', 'integration')

    # Run unit tests
    # unit_test_command = ["pytest", "--color=yes", unit_test_dir]
    # command = [sys.executable, "-m", "pytest", "--color=yes", "."]
    # print(os.getcwd())
    # print(unit_test_command)
    # try:
    #     print("run_all_tests called 3")
    #     result = subprocess.run(unit_test_command, check=True, capture_output=True, text=True)
    #     logging.info(f"Successfully executed command: {' '.join(unit_test_command)}")
    #     print(result.stdout)
    # except subprocess.CalledProcessError as e:
    #     logging.error(f"Error running unit tests: {e}")
    #     logging.error(f"Command output: {e.output}")
    #     logging.error(f"Command error: {e.stderr}")
    #     print(f"Error running unit tests: {e}")
    #     print(f"Command output: {e.output}")
    #     print(f"Command error: {e.stderr}")
    #     sys.exit(1)

    # # Run integration tests
    # integration_test_command = ["pytest", "--color=yes", integration_test_dir]
    # try:
    #     result = subprocess.run(integration_test_command, check=True, capture_output=True, text=True)
    #     logging.info(f"Successfully executed command: {' '.join(integration_test_command)}")
    #     print("Hello from integration test!")
    #     print(result.stdout)
    # except subprocess.CalledProcessError as e:
    #     logging.error(f"Error running integration tests: {e}")
    #     logging.error(f"Command output: {e.output}")
    #     logging.error(f"Command error: {e.stderr}")
    #     print(f"Error running integration tests: {e}")
    #     print(f"Command output: {e.output}")
    #     print(f"Command error: {e.stderr}")
    #     sys.exit(1)