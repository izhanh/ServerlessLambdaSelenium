#!/bin/bash

# Install dependencies
npm install serverless
npm install serverless-python-requirements
apt install -y virtualenv

# Run virutal environment
virtualenv -p python3 venv
source venv/bin/activate

# Install PIP inside the env
pip install -r requirements.txt