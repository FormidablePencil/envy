#!/bin/bash

# Check if the module name is provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 module_name"
    exit 1
fi

MODULE_NAME="$1"

# Execute the Python module
python3 -m "$MODULE_NAME"
