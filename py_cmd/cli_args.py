import argparse
from enum import Enum, auto

class CommandLineArgs(Enum):
    target = auto()
    pythonpath = auto()
    test = auto()
    test_a = auto()
    unit_test = auto()
    unit_test_a = auto()
    integration_test = auto()
    integration_test_a = auto()
    execute_task = auto()
    generate_from_anywhere = auto()
    apply_changes_from_anywhere = auto()

# Example usage:
def get_arg_description(arg):
    def append_adressing_variant_a(is_a: bool):
        return f'also {'NOT' if not is_a else ""} including target test file.'

    descriptions = {
        CommandLineArgs.target: 'The Python script, directory of tests, or task to execute.',
        CommandLineArgs.pythonpath: 'The PYTHONPATH to set.',
        CommandLineArgs.test: 'Run all tests (unit and integration) ' + append_adressing_variant_a(False),
        CommandLineArgs.test_a: 'Run all tests (unit and integration) ' + append_adressing_variant_a(True),
        CommandLineArgs.unit_test: 'Run unit tests only ' + append_adressing_variant_a(False),
        CommandLineArgs.unit_test_a: 'Run unit tests only ' + append_adressing_variant_a(True),
        CommandLineArgs.integration_test: 'Run integration tests only ' + append_adressing_variant_a(False),
        CommandLineArgs.integration_test_a: 'Run integration tests only ' + append_adressing_variant_a(True),
        CommandLineArgs.execute_task: 'Execute a task using the CentralAIManager.',
        CommandLineArgs.generate_from_anywhere: 'Generate code from anywhere using the CentralAIManager.',
        CommandLineArgs.apply_changes_from_anywhere: 'Apply changes from anywhere using the CentralAIManager.',
    }
    return descriptions.get(arg, "No description available.")

## Example of accessing the enum and its description
#for arg in CommandLineArgs:
#    print(f"{arg.name}: {get_arg_description(arg)}")

def set_cli_args(argparse: argparse) -> CommandLineArgs:
    parser = argparse.ArgumentParser(description='Run a Python script, test suite, or AI-powered codebase operations.')
    parser.add_argument('target', nargs='?', default=None, help=get_arg_description(CommandLineArgs.target))
    parser.add_argument('-p', '--pythonpath', default=None, help=get_arg_description(CommandLineArgs.pythonpath))
    parser.add_argument('-t', '--test', action='store_true', help=get_arg_description(CommandLineArgs.test))
    parser.add_argument('-ut', '--unit-test', action='store_true', help=get_arg_description(CommandLineArgs.unit_test))
    parser.add_argument('-uta', '--unit-test-also', action='store_true', help=get_arg_description(CommandLineArgs.unit_test_a))
    parser.add_argument('-it', '--integration-test', action='store_true', help=get_arg_description(CommandLineArgs.integration_test))
    parser.add_argument('-ita', '--integration-test-also', action='store_true', help=get_arg_description(CommandLineArgs.integration_test_a))
    parser.add_argument('-e', '--execute-task', action='store_true', help=get_arg_description(CommandLineArgs.execute_task))
    parser.add_argument('-g', '--generate-from-anywhere', action='store_true', help=get_arg_description(CommandLineArgs.generate_from_anywhere))
    parser.add_argument('-a', '--apply-changes-from-anywhere', action='store_true', help=get_arg_description(CommandLineArgs.apply_changes_from_anywhere))
    return parser.parse_args()
