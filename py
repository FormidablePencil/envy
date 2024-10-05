#!/usr/bin/env python3
import os
import sys
import subprocess
import argparse
import logging
from pathlib import Path
from central_ai_manager.main import CentralAIManager
from ai_components.neural_network import NeuralNetwork
from central_ai_manager.main import ConvolutionalNeuralNetworkComponent, RecurrentNeuralNetworkComponent, TransformerNetworkComponent

# Configure logging
logging.basicConfig(filename='py_script_execution.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def set_pythonpath(path):
    """Sets the PYTHONPATH environment variable."""
    if path:
        os.environ["PYTHONPATH"] = path
        logging.info(f"PYTHONPATH set to: {path}")
    else:
        os.environ["PYTHONPATH"] = "envy"
        logging.info(f"PYTHONPATH set to default: envy")

def run_tests(target_path, test_type):
    """Runs the specified test type for the given target."""
    if test_type == 'integration':
        test_dir = os.path.join(os.path.dirname(target_path), 'integration')
        logging.info(f"Running integration tests in directory: {test_dir}")
        test_pattern = os.path.basename(target_path)
    elif test_type == 'unit':
        test_file = TEST_MAPPING.get(os.path.basename(target_path), {}).get('unit')
        if test_file:
            test_dir = os.path.join(os.path.dirname(target_path), 'unit')
            logging.info(f"Running unit tests for file: {test_file}")
            test_pattern = os.path.basename(test_file)
        else:
            test_dir = os.path.join(os.path.dirname(target_path), 'unit')
            logging.info(f"Running unit tests in directory: {test_dir}")
            test_pattern = '*.py'
    else:
        raise ValueError(f"Invalid test type: {test_type}")

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

def run_all_tests():
    """Runs all tests (unit and integration) in the 'tests' directory."""
    unit_test_dir = os.path.join(os.getcwd(), 'tests', 'unit')
    integration_test_dir = os.path.join(os.getcwd(), 'tests', 'integration')

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

def execute_task(task: dict):
    """Executes a task using the CentralAIManager and registered AI components."""
    central_ai_manager = CentralAIManager()
    
    # Register AI components
    neural_net_component = NeuralNetworkComponent("MyNeuralNet")
    cnn_component = ConvolutionalNeuralNetworkComponent("MyCNN")
    rnn_component = RecurrentNeuralNetworkComponent("MyRNN")
    transformer_component = TransformerNetworkComponent("MyTransformer")
    central_ai_manager.register_ai_component(neural_net_component)
    central_ai_manager.register_ai_component(cnn_component)
    central_ai_manager.register_ai_component(rnn_component)
    central_ai_manager.register_ai_component(transformer_component)

    # Execute the task
    central_ai_manager.execute_task(task)

def generate_code_from_anywhere(task: dict):
    """Generates code from anywhere using the CentralAIManager."""
    central_ai_manager = CentralAIManager()
    file_path = central_ai_manager.generate_from_anywhere(task)
    return file_path

def apply_changes_from_anywhere(file_path: str):
    """Applies changes from anywhere using the CentralAIManager."""
    central_ai_manager = CentralAIManager()
    central_ai_manager.apply_changes_from_anywhere(file_path)

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
            os.chdir(os.path.dirname(args.target))
            try:
                result = subprocess.run([sys.executable, os.path.basename(args.target)], check=True, capture_output=True, text=True)
                logging.info(f"Successfully executed command: {sys.executable} {os.path.basename(args.target)}")
                print(result.stdout)
            except subprocess.CalledProcessError as e:
                logging.error(f"Error running script: {e}")
                logging.error(f"Command output: {e.output}")
                logging.error(f"Command error: {e.stderr}")
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

    pythonpath = args.pythonpath
    set_pythonpath(pythonpath)

if __name__ == "__main__":
    main()