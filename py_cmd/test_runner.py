import os
import sys
import subprocess
import logging
import posixpath
from enum import Enum, auto
from tests.test_mapping import TEST_MAPPING
from cli_args import CommandLineArgs

class Py_cmd_util(Enum):
    def msg(self):
        return self.value[0]

    ONLY_ONE_TEST_ARG = ("""
        Exactly one of test, integration_test, or unit_test must be true for arg./ 
        Only one test flag is allowed (e.g. -t, -ut or -it).
        """)
    def test_args_amount(self):
        return self.value[1]
    def set_test_args_amount(self, arg):
        self.value[1] = arg

    NO_ARGS_REG = "No 'reg' variant test flag provided."
    def do_args_reg_exist(self, args: CommandLineArgs) -> bool:
        return args.test or args.integration_test or args.unit_test
    
    NO_ARGS_A = "No 'a' variant test flag provided."
    def do_args_a_exist(self, args: CommandLineArgs) -> bool:
        return args.test_a or args.integration_test_a or args.unit_test_a

class CustomAssertionError(Exception):
    def __init__(self, message, arg):
        super().__init__(message)
        self.arg = arg

def py_cmd_assert(condition, py_cmd_err: Py_cmd_util):
    if not condition:
        raise CustomAssertionError(py_cmd_err.msg, py_cmd_err[1])

"""Runs tests (either unit, integration or both)."""
class run_tests_associated_to_target:
    def execute_command(command):
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

    def _assert_args_reg_exist(args: CommandLineArgs) -> bool:
        assert Py_cmd_util.do_args_reg_exist(args), Py_cmd_util.NO_ARGS_REG
        return True
    def _assert_args_a_exist(args: CommandLineArgs) -> bool:
        assert Py_cmd_util.do_args_a_exist(args), Py_cmd_util.NO_ARGS_A
        return True
    def _do_args_reg_exist(args: CommandLineArgs) -> bool:
        return Py_cmd_util.do_args_reg_exist(args)
    def _do_args_a_exist(args: CommandLineArgs) -> bool:
        return Py_cmd_util.do_args_a_exist(args)

    def _only_one_test_flag(flags: CommandLineArgs):
        test_flags_reg = sum([
            flags.test,
            flags.integration_test,
            flags.unit_test
        ])
        test_flags_a = sum([
            flags.test_a,
            flags.integration_test_a,
            flags.unit_test_a
        ])
        test_flags = sum([
            flags.test or flags.test_a,
            flags.integration_test or flags.integration_test_a,
            flags.unit_test or flags.unit_test_a
        ])
        assert (test_flags_reg == 1 and test_flags_a == 0) or (test_flags_reg == 0 and test_flags_a == 1), f"0~ /
            Can't use both a variant and not a variant test flag"
        assert test_flags_reg > 1 or test_flags_a > 1, f"0~ /
            Only 1 test flag allowed (unless if chained which is a todo item)." # TODO Implement chained py commands
        py_cmd_assert(test_flags == 1, Py_cmd_util.ONLY_ONE_TEST_ARG.set_test_args_amount(test_flags))

    def _run_file(self, args):
        self._only_one_test_flag(args)

        unit_test_dir = os.path.join(args.target, 'tests', 'unit')
        integration_test_dir = os.path.join(args.target, 'tests', 'integration')
        unit_test_command = ["pytest", "--color=yes", unit_test_dir]
        integration_test_command = ["pytest", "--color=yes", integration_test_dir]

        run()
        def run():
            if args.test:
                # Run the right type of tests respectfully then reset test args back
                logging.info(f"Will run all tests in directories: {unit_test_dir}, {integration_test_dir}")
                args.test = False
                args.integration_test = True
                args.unit_test = True
                run()
                args.test = True
                args.integration_test = False
                args.unit_test = False
            if args.integration_test:
                logging.info(f"Running integration tests for {args.target}. Test: {test}")
                logging.info(f"Running integration tests in directory: {integration_test_dir}")
                self.execute_command(integration_test_command)
            if args.unit_test:
                logging.info(f"Running unit tests in directory: {unit_test_dir}")
                self.execute_command(unit_test_command)

    def _run_dir(self, args):
        self._only_one_test_flag(args)

        unit_test_dir = os.path.join(args.target, 'tests', 'unit')
        integration_test_dir = os.path.join(args.target, 'tests', 'integration')
        unit_test_command = ["pytest", "--color=yes", unit_test_dir]
        integration_test_command = ["pytest", "--color=yes", integration_test_dir]

        class Test_commands:
            class Test_type(Enum):
                DIR = auto(), FILE = auto()
            command = ""
            test_type: Test_type

            def __init__(self, test_type: Test_type):
                self.test_type = test_type
                match test_type:
                    case DIR:
                        self.command = 
                    case FILE:
                        self.command = 

            def run_integration():
                if 
                logging.info(f"Running integration tests for {args.target}. Test: {test}")
                logging.info(f"Running integration tests in directory: {integration_test_dir}")
                self.execute_command(integration_test_command)
            def run_unit():
        run(False)
        def run(run_file: bool, test_commands: Test_commands):
            if args.test:
                # Run the right type of tests respectfully then reset test args back
                # TODO address run_file here
                logging.info(f"Will run all tests in directories: {unit_test_dir}, {integration_test_dir}")
                args.test = False
                args.integration_test = True
                args.unit_test = True
                run()
                args.test = True
                args.integration_test = False
                args.unit_test = False
            if args.integration_test:
                logging.info(f"Running integration tests for {args.target}. Test: {test}")
                logging.info(f"Running integration tests in directory: {integration_test_dir}")
                self.execute_command(integration_test_command)
            if args.unit_test:
                logging.info(f"Running unit tests in directory: {unit_test_dir}")
                self.execute_command(unit_test_command)

    """Run against current working directory"""
    def cwd(self, args):
        assert args.target, f"0~ Should not have access to whatever is in args.target: {args.target}"
        args.target = os.getcwd()
        self._run_dir(args)
        args.target = None

# print(os.getcwd()) # TODO: os.getcwd() may need to be called before cwd is set and passed in through func arg

    def dir(self, args):
        assert os.path.isdir(args.target), f"0~ args.target: {args.target} is not a directory."
        self._run_dir(args)

# todo: handle executing with flags -t, -it and -ut against a directory which will execute tests assiciated
# to files in that directory
# todo: also handle executin against a regular executable file and a unit test file
# ececuting with or wtihout flags against a regular and test file should be handled respectfully

    def file(self, args: CommandLineArgs):
        try:
            self._only_one_test_flag(args)
        except CustomAssertionError as e:
            assert e is Py_cmd_util.ONLY_ONE_TEST_ARG and e.arg is 0, f"""0~
                There are '{e.arg}' test flags which should have been 0 or 1 when executing
                py command against a file. 0 test flags if you're trying to run against a
                test file or 1 test flag to run associated tests to target test file. Use
                -uta or -ita to run the target test file as well as the tests associated 
                to the target file.
                """
                # If passed then run the file as a unit test rather than running all files associated to 
        assert os.path.isfile(args.target), f"0~ args.target: {args.target} is not a file."

        if args.target.startswith('test_'):
            # If target is a test file but with a test flag provided then run tests associated to the target test 
            if self._assert_args_reg_exist:
                self._run_dir(args)
            if self._assert_args_a_exist:
                file_args = CommandLineArgs().target = args.target
                self.file(file_args)
                self._run_dir(args)
            elif not self._do_args_reg_exist(args) or not self._do_args_a_exist(args):
                # Otherwise if no test related flag was provided then just run target test file as a test (with pytest)
                self.execute_command()
                # Run the specific test file
                test_type_of_available_files = os.path.dirname(args.target)
                test_pattern = os.path.basename(args.target)
                # Run the tests
                command = ["pytest", "--color=yes", test_type_of_available_files, "-k", test_pattern]
                self.execute_command(command)

        # If target is a regular Python file then run tests associated to file (but won't run target file itself)
        elif not args.target.startswith('test_'):
            assert not self._do_args_a_exist(), f"You can't run target file as a test \
                file. Command with some 'a' test flag variant was supplied which is \
                reserved for running tests along with the target test file which in \
                this case the target file wasn't a test file or the target file doesn't \
                follow the file naming standard for tests files to be prefixed with 'test_'"
            # Find the corresponding test file(s) for the target file
            # Run this only when -t is provided:
            # test_type_of_available_files = os.path.dirname(target_path)
            test_pattern = os.path.basename(args.target)
            target_dir = posixpath.basename(posixpath.dirname(args.target))
            tests_of_types = []
            if args.test:
                tests_of_types.append(TEST_MAPPING.get(target_dir).get(test_pattern, []).get('integration', [])) # TODO Remove []
                tests_of_types.append(TEST_MAPPING.get(target_dir, []).get(test_pattern, []).get("unit", [])) # TODO Remove []
            elif args.integration_test:
                tests_of_types.append(TEST_MAPPING.get(target_dir).get(test_pattern, []).get('integration', [])) # TODO Remove []
            elif args.unit_test:
                tests_of_types.append(TEST_MAPPING.get(target_dir, []).get(test_pattern, []).get("unit", [])) # TODO Remove []
            for tests in tests_of_types:
                for test in tests:
                    print(test, "tests")
                    if test_type == 'integration':
                        logging.info(f"Running integration tests for {target_path}. Test: {test}")
                        # Run the tests
                        command = ["pytest", "--color=yes", test]
                        self.execute_command(command)
                    elif test_type == 'unit':
                        logging.info(f"Running unit tests for {target_path}. Test: {test}")
                        # Run the tests
                        command = ["pytest", "--color=yes", test]
                        self.execute_command(command)
                    else:
                        raise Exception(f"Invalid test type: {test_type}, Test type of available files: {test}")
        else:
            logging.error(f"Error: The specified target '{args.target}' is not a valid file or directory.")
            print(f"Error: The specified target '{args.target}' is not a valid file or directory.")
            sys.exit(1)
            

        # target_dir = posixpath.basename(posixpath.dirname(args.target))
        # unit_test_dir = os.path.join(target_dir, 'tests', 'unit')
        # integration_test_dir = os.path.join(target_dir, 'tests', 'integration')

        ## if not directory ofcourse
        # run_tests(target, "integration")
        # run_tests(target_path, "unit")

    def _file_deprecated(self, target_path, test_type):
        """Runs the specified test type for the given target."""
        print(f"run_tests called with target_path: {target_path}")
        if os.path.isfile(target_path) and not target_path.startswith('test_'):
            # Find the corresponding test file(s) for the target file
            # Run this only when -t is provided:
            # test_type_of_available_files = os.path.dirname(target_path)
            test_pattern = os.path.basename(target_path)
            target_dir = posixpath.basename(posixpath.dirname(target_path))
            if test_type == 'integration':
                tests = TEST_MAPPING.get(target_dir).get(test_pattern, []).get('integration', [])
            if test_type == 'unit':
                tests = TEST_MAPPING.get(target_dir, []).get(test_pattern, []).get("unit", [])

            print(tests, "kk tests")
            for test in tests:
                print(test, "tests")
                if test_type == 'integration':
                    logging.info(f"Running integration tests for {target_path}. Test: {test}")
                    # Run the tests
                    command = ["pytest", "--color=yes", test]
                    self.execute_command(command)
                elif test_type == 'unit':
                    logging.info(f"Running unit tests for {target_path}. Test: {test}")
                    # Run the tests
                    command = ["pytest", "--color=yes", test]
                    self.execute_command(command)
                else:
                    raise Exception(f"Invalid test type: {test_type}, Test type of available files: {test}")
        # elif os.path.isfile(target_path) and target_path.startswith('test_'):
        #     # Run the specific test file
        #     test_type_of_available_files = os.path.dirname(target_path)
        #     test_pattern = os.path.basename(target_path)
        #     # Run the tests
        #     command = ["pytest", "--color=yes", test_type_of_available_files, "-k", test_pattern]
        #     self.execute_command(command)
        # elif os.path.isdir(target_path):
        #     print(f"run_tests called with directory target_path: {target_path}")
        #     if target_path == os.path.join(os.getcwd(), 'py'):
        #         # Run all tests in the py/tests directory
        #         unit_test_dir = os.path.join(target_path, 'tests', 'unit')
        #         integration_test_dir = os.path.join(target_path, 'tests', 'integration')
        #     else:
        #         # Run all tests in the envy/ directory
        #         unit_test_dir = os.path.join(os.getcwd(), 'tests', 'unit')
        #         integration_test_dir = os.path.join(os.getcwd(), 'tests', 'integration')

        #     if test_type == 'unit':
        #         command = ["pytest", "--color=yes", unit_test_dir]
        #         logging.info(f"Running unit tests in directory: {unit_test_dir}")
        #     elif test_type == 'integration':
        #         command = ["pytest", "--color=yes", integration_test_dir]
        #         logging.info(f"Running integration tests in directory: {integration_test_dir}")
        #     else:
        #         command = ["pytest", "--color=yes", unit_test_dir, integration_test_dir]
        #         logging.info(f"Running all tests in directories: {unit_test_dir}, {integration_test_dir}")
        #     self.execute_command(command)
        # else:
        #     logging.error(f"Error: The specified target '{target_path}' is not a valid file or directory.")
        #     print(f"Error: The specified target '{target_path}' is not a valid file or directory.")
        #     sys.exit(1)