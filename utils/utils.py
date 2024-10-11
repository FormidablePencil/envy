import subprocess
import logging

def is_empty(arg):
    if arg is None:
        return True
    if isinstance(arg, (str, list, tuple, dict)):
        return len(arg) == 0
    return False

def execute_command(command, input=None):
    """
    Execute a CLI command and return the output.
    """
    try:
        if input:
            result = subprocess.run(command, shell=True, capture_output=True, text=True, input=input, check=True)
        else:
            result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        logging.error(f"Error executing command: {e}")
        return f"Error executing command: {e}"

def log_message(message, level=logging.INFO):
    """
    Log a message to the console.
    """
    if level == logging.INFO:
        logging.info(message)
    elif level == logging.ERROR:
        logging.error(message)
    elif level == logging.DEBUG:
        logging.debug(message)
    else:
        logging.warning(message)