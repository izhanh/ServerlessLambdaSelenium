#!/bin/bash

# Unzip Chrome if not done already
if [ ! -d directory ]; then 
	unzip chrome.zip
fi

# Set AWS
source aws.properties
sed -i '/export AWS_PROFILE/d' ~/.bashrc
sed -i '/export AWS_PROFILE/d' /etc/profile
echo "export AWS_PROFILE=izhan && export AWS_REGION=eu-west-1" >> ~/.bashrc
echo "export AWS_PROFILE=izhan && export AWS_REGION=eu-west-1" >> /etc/profile

# Run virutal environment
virtualenv -p python3 venv
source venv/bin/activate

# Install dependencies
npm install -g serverless
npm install -g serverless-python-requirements
apt install -y virtualenv

# Install PIP inside the env
pip install -r requirements.txt