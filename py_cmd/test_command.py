import os
import logging
from enum import Enum, auto
from cli_args import CommandLineArgs
from typing import TypedDict, Optional, Generic, TypeVar
from dataclasses import dataclass
from typing import Callable

# these go one level up of abstraction
    # def setup_rerun_path():
    #     logging.info(f"Will run all tests in directories: {self.commands.unit_test_dir}, {self.commands.integration_test_dir}")
    #     args.test = False
    #     args.integration_test = True
    #     args.unit_test = True
    
    # def reset_path():
    #     args.test = True
    #     args.integration_test = False
    #     args.unit_test = False

    def run(
        self, args: CommandLineArgs,
        cases: list[CaseCodePath],
        test_call: Callable[[any], any] = None,
        integration_test_call: Callable[[any], any] = None,
        unit_test_call: Callable[[any], any] = None,
        ):

        if args.test:
            test_call()
            # Run the appropriate tests, then reset the test arguments.
            setup_rerun_test_path()
            self.run_test_path()
            reset_test_path()
        if args.integration_test:
            integration_test_call()
            match self.test_type:
                case self.Test_type.DIR:
                    logging.info(f"Running integration tests in directory: {self.commands.integration_test_dir}")
                case self.Test_type.FILE:
                    logging.info(f"Running integration tests for {args.target}. Test: {test}")
            # TODO
            self.execute_command(self.commands.integration_test_command)
        if args.unit_test:
            unit_test_call()
            match self.test_type:
                case self.Test_type.DIR:
                    logging.info(f"Running unit tests in directory: {self.test_dirs.unit_test_dir}")
                case self.Test_type.FILE:
                    pass
            # TODO
            self.execute_command(self.commands.unit_test_command)


# @dataclass
# class Test_dirs:
#     unit_test_dir: Optional[str]
#     integration_test_dir: Optional[str]

class Test_commands:
    class Test_type(Enum):
        DIR = auto(), FILE = auto()

    class Test_dirs(TypedDict):
        unit_test_dir: Optional[str]
        integration_test_dir: Optional[str]

    class Commands(TypedDict):
        unit_test_command: Optional[str]
        integration_test_command: Optional[str]

    test_type: Test_type
    test_dirs: Test_dirs
    commands: Commands
    execute_command: Callable[[CommandLineArgs], None]

    def __init__(
            self,
            test_type: Test_type,
            args: CommandLineArgs,
            execute_command: Callable[[CommandLineArgs], None]
        ):
        self.test_type = test_type
        if args.test:
        if args.integration_test:
        if args.unit_test:
        self.test_dirs.unit_test_dir = os.path.join(args.target, 'tests', 'unit')
        self.test_dirs.integration_test_dir = os.path.join(args.target, 'tests', 'integration')
        self.commands.unit_test_command = ["pytest", "--color=yes", self.test_dirs.unit_test_dir]
        self.commands.integration_test_command = ["pytest", "--color=yes", self.test_dirs.integration_test_dir]
        self.execute_command = execute_command

    def run_test_path(
            self, args: CommandLineArgs,
            test_call: Callable[[any], any] = None,
            integration_test_call: Callable[[any], any] = None,
            unit_test_call: Callable[[any], any] = None,
        ):
        def setup_rerun_test_path():
            logging.info(f"Will run all tests in directories: {self.commands.unit_test_dir}, {self.commands.integration_test_dir}")
            args.test = False
            args.integration_test = True
            args.unit_test = True
        
        def reset_test_path():
            args.test = True
            args.integration_test = False
            args.unit_test = False

        if args.test:
            test_call()
            # Run the appropriate tests, then reset the test arguments.
            setup_rerun_test_path()
            self.run_test_path()
            reset_test_path()
        if args.integration_test:
            integration_test_call()
            match self.test_type:
                case self.Test_type.DIR:
                    logging.info(f"Running integration tests in directory: {self.commands.integration_test_dir}")
                case self.Test_type.FILE:
                    logging.info(f"Running integration tests for {args.target}. Test: {test}")
            # TODO
            self.execute_command(self.commands.integration_test_command)
        if args.unit_test:
            unit_test_call()
            match self.test_type:
                case self.Test_type.DIR:
                    logging.info(f"Running unit tests in directory: {self.test_dirs.unit_test_dir}")
                case self.Test_type.FILE:
                    pass
            # TODO
            self.execute_command(self.commands.unit_test_command)

        match test_type:
            case self.Test_type.DIR:
                self.commands.append(unit_test_command)
                self.commands.append(integration_test_command)
                self.log_info = 
            case self.Test_type.FILE:
                self.command = 

    def log_running_tests_against_dir(): 
        logging.info(f"Running integration tests in directory: {integration_test_dir}")

    def log_running_tests_associated_to_target(): 
        logging.info(f"Running integration tests for {args.target}. Test: {test}")

    def ex_cmd(self):
        self.execute_command(self.command)

    def run_integration():
        if 
        logging.info(f"Running integration tests for {args.target}. Test: {test}")
        logging.info(f"Running integration tests in directory: {integration_test_dir}")
        self.execute_command(integration_test_command)
    def run_unit():