#!/bin/zsh

# Activate the virtual environment
source myenv/bin/activate

# Read the string from a local file (e.g., input.txt)
input_string=$(cat input.txt)

# Run the Python script and pass the string as an argument
python request.py "$input_string"

# Deactivate the virtual environment
deactivate