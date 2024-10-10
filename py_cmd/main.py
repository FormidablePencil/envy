import os
import sys
import subprocess
import argparse
sys.path.append('/home/formidablepencil/envy')
from py_cmd.cli import main as cli_main

if __name__ == "__main__":
    # print("fk")
    # os.chdir(os.environ.get("py_PYTHONPATH", "envy"))
    # from .cli import main as cli_main
    # from .util import set_pythonpath
    cli_main()

####!/usr/bin/env python3