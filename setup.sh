#!/bin/bash
# Run this script to install your virtual environment with all dependencies
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt