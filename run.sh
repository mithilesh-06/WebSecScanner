#!/bin/bash
echo "Setting up virtual environment..."
python3 -m venv venv
source venv/bin/activate

echo "Installing dependencies..."
pip install flask google-generativeai requests

echo "Starting the server..."
python backend/app.py
