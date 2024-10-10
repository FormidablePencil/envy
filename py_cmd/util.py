import os
import logging

def set_pythonpath(path):
    """Sets the PYTHONPATH environment variable."""
    if path:
        os.environ["PYTHONPATH"] = path
        logging.info(f"PYTHONPATH set to: {path}")
    else:
        os.chdir(os.environ.get("py_PYTHONPATH", "envy"))
        logging.info(f"PYTHONPATH set to default: envy")
