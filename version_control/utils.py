import subprocess

def execute_command(command):
    """
    Execute a CLI command and return the output.
    """
    return subprocess.check_output(command, shell=True, universal_newlines=True)

def log_message(message):
    """
    Log a message to the console.
    """
    print(message)