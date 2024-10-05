#!/bin/bash

# Check if a Python script is provided as an argument
if [ -z "$1" ]; then
  echo "Error: Please provide a Python script as an argument."
  exit 1
fi

# Construct the full path to the Python script
script_path=$(realpath "$1")

# Check if the script exists
if [ ! -f "$script_path" ]; then
  echo "Error: Python script '$1' not found."
  exit 1
fi

# Set PYTHONPATH based on command-line arguments
if [[ "$2" == "-p" || "$2" == "--pythonpath" ]]; then
  PYTHONPATH="$3"
  shift 3
else
  PYTHONPATH="envy"
fi

# Run the py command with the PYTHONPATH set in the environment
env PYTHONPATH="$PYTHONPATH" py "$script_path"
