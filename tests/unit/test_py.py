import pytest
import subprocess
import os
import sys

def run_py_command(args, pythonpath):
    try:
        os.environ["PYTHONPATH"] = pythonpath
        result = subprocess.run(["py"] + args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error running py command: {e}"

def test_py_command_sets_pythonpath():
    run_py_command([ "-c", "pass" ], ".")
    assert os.environ["PYTHONPATH"] == "."

def test_py_command_sets_custom_pythonpath():
    run_py_command([ "-c", "pass" ], "Outer_dir")
    assert os.environ["PYTHONPATH"] == "Outer_dir"

def test_py_command_runs_script():
    script_content = "print('Hello, world!')"
    with open("test_script.py", "w") as f:
        f.write(script_content)
    output = run_py_command(["test_script.py"], "envy")
    assert "Hello, world!" in output
    os.remove("test_script.py")

if __name__ == "__main__":
    pytest.main(["-v", __file__])
