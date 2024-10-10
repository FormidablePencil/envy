import pytest
import subprocess
import os
import sys
from cli import main as cli_main

def test_py_cli_runs_tests_integration():
    try:
        result = subprocess.run(["py", "py/main.py", "-t"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        assert "Successfully executed command" in result.stdout
    except subprocess.CalledProcessError as e:
        assert False, f"Error running tests: {e.stderr}"

def test_py_cli_runs_unit_tests_integration():
    try:
        result = subprocess.run(["py", "py/main.py", "-ut"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        assert "Successfully executed command" in result.stdout
    except subprocess.CalledProcessError as e:
        assert False, f"Error running unit tests: {e.stderr}"

def test_py_cli_runs_integration_tests_integration():
    try:
        result = subprocess.run(["py", "py/main.py", "-it"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        assert "Successfully executed command" in result.stdout
    except subprocess.CalledProcessError as e:
        assert False, f"Error running integration tests: {e.stderr}"

def test_py_cli_executes_task_integration():
    try:
        result = subprocess.run(["py", "py/main.py", "-e"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        assert "Task executed successfully" in result.stdout
    except subprocess.CalledProcessError as e:
        assert False, f"Error executing task: {e.stderr}"

def test_py_cli_generates_code_integration():
    try:
        result = subprocess.run(["py", "py/main.py", "-g"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        assert "Generated code written to" in result.stdout
    except subprocess.CalledProcessError as e:
        assert False, f"Error generating code: {e.stderr}"

def test_py_cli_applies_changes_integration():
    try:
        result = subprocess.run(["py", "py/main.py", "-a", "some_file.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        assert "Changes applied successfully" in result.stdout
    except subprocess.CalledProcessError as e:
        assert False, f"Error applying changes: {e.stderr}"