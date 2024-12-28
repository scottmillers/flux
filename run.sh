#!/bin/zsh


# Read the string from a local file (e.g., input.txt)
#input_string=$(cat flux-io/vlogger.txt)
#filename="flux-io/vlogger.jpg"

input_string=$(cat flux-io/dragon.txt)
filename="flux-io/dragon.jpg"

# Run the Python script and pass the string as an argument
python request.py "$input_string" "$filename"
