#!/bin/bash
# This script creates a virtual environment and installs the required packages for the project.
# Check if the virtual environment already exists
if [ -d ".venv" ]; then
    echo "Virtual environment already exists. Activating it..."
else
    echo "Creating virtual environment..."
    python3 -m venv .venv
    echo "Virtual environment created."
fi
# Activate the virtual environment
source .venv/bin/activate
echo "Virtual environment activated."
# Install the required packages
if [ -f "requirements.txt" ]; then
    echo "Installing required packages..."
    pip install -r requirements.txt
    echo "Required packages installed."
else
    echo "requirements.txt not found. Please create a requirements.txt file with the required packages."
fi

python run.py