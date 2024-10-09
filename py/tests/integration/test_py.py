import pytest
import subprocess
import os
import sys
import logging

logging.basicConfig(level=logging.INFO)

def run_integration_test(args, pythonpath):
    try:
        os.environ["PYTHONPATH"] = pythonpath
        logging.info(f"Running integration test with args: {args}")
        result = subprocess.run(["py"] + args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        logging.info(f"Integration test output: {result.stdout.strip()}")
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        logging.error(f"Error running integration test: {e}")
        logging.error(f"Command output: {e.output}")
        logging.error(f"Command error: {e.stderr}")
        return f"Error running integration test: {e}"

def test_integration_py_command_sets_pythonpath():
    run_integration_test([ "-c", "pass" ], ".")
    assert os.environ["PYTHONPATH"] == "."

def test_integration_py_command_sets_custom_pythonpath():
    run_integration_test([ "-c", "pass" ], "Outer_dir")
    assert os.environ["PYTHONPATH"] == "Outer_dir"

def test_integration_py_command_runs_integration_test_for_file():
    script_content = "print('Hello from integration test!')"
    with open("integration_test_script.py", "w") as f:
        f.write(script_content)
    output = run_integration_test(["integration_test_script.py"], "envy")
    assert "Hello from integration test!" in output
    os.remove("integration_test_script.py")

def test_integration_py_command_runs_integration_tests_for_directory():
    script_content = "print('Hello from integration test!')"
    with open("integration_test_script.py", "w") as f:
        f.write(script_content)
    output = run_integration_test(["-it", "tests/integration"], "envy")
    logging.info(f"Integration test output: {output}")
    assert "Hello from integration test!" in output
    os.remove("integration_test_script.py")

def test_integration_py_command_handles_invalid_target():
    try:
        run_integration_test(["non_existent_script.py"], "envy")
    except subprocess.CalledProcessError as e:
        assert "Error running integration test" in str(e)

if __name__ == "__main__":
    pytest.main(["-v", __file__])