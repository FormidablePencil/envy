import os
import sys
import subprocess
import logging
from utils import set_pythonpath
from tests.test_mapping import TEST_MAPPING

def run_tests(target_path, test_type):
    """Runs the specified test type for the given target."""
    if os.path.isfile(target_path) and not target_path.startswith('test_'):
        # Find the corresponding test file(s) for the target file
        test_files = TEST_MAPPING.get(os.path.dirname(target_path) + "/", {}).get(os.path.basename(target_path), [])
        for test_file in test_files:
            if test_type == 'integration':
                test_dir = os.path.join(os.path.dirname(__file__), os.path.dirname(test_file))
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
                test_dir = os.path.join(os.path.dirname(__file__), os.path.dirname(test_file))
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
        # Run all tests in the unit and integration test directories
        unit_test_dir = os.path.join(target_path, 'tests', 'unit')
        integration_test_dir = os.path.join(target_path, 'tests', 'integration')

        # Check if pytest is installed, and install it if not
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "show", "pytest"])
        except subprocess.CalledProcessError:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "pytest"])

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

def run_all_tests():
    """Runs all tests (unit and integration) in the 'tests' directory."""
    unit_test_dir = os.path.join(os.getcwd(), 'tests', 'unit')
    integration_test_dir = os.path.join(os.getcwd(), 'tests', 'integration')

    # Check if pytest is installed, and install it if not
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "show", "pytest"])
    except subprocess.CalledProcessError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pytest"])

    # Run unit tests
    unit_test_command = ["pytest", "--color=yes", unit_test_dir]
    try:
        result = subprocess.run(unit_test_command, check=True, capture_output=True, text=True)
        logging.info(f"Successfully executed command: {' '.join(unit_test_command)}")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        logging.error(f"Error running unit tests: {e}")
        logging.error(f"Command output: {e.output}")
        logging.error(f"Command error: {e.stderr}")
        print(f"Error running unit tests: {e}")
        print(f"Command output: {e.output}")
        print(f"Command error: {e.stderr}")
        sys.exit(1)

    # Run integration tests
    integration_test_command = ["pytest", "--color=yes", integration_test_dir]
    try:
        result = subprocess.run(integration_test_command, check=True, capture_output=True, text=True)
        logging.info(f"Successfully executed command: {' '.join(integration_test_command)}")
        print("Hello from integration test!")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        logging.error(f"Error running integration tests: {e}")
        logging.error(f"Command output: {e.output}")
        logging.error(f"Command error: {e.stderr}")
        print(f"Error running integration tests: {e}")
        print(f"Command output: {e.output}")
        print(f"Command error: {e.stderr}")
        sys.exit(1)