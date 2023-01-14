#!/bin/bash
echo "****************************************"
echo " Setting up bx Environment"
echo "****************************************"

echo "Updating package manager..."
sudo add-apt-repository -y ppa:deadsnakes/ppa

echo "Installing Python 3.8 and Virtual Environment"
sudo apt-get update
sudo DEBIAN_FRONTEND=noninteractive apt-get install -y python3.8 python3.8-venv

echo "Creating a Python virtual environment"
python3.8 -m venv bxenv

echo "Checking the Python version..."
python3 --version

echo "Installing Python depenencies..."
source bxenv/bin/activate && python3 -m pip install --upgrade pip wheel
source bxenv/bin/activate && pip install -r ./brandxpert/requirements.txt

echo "****************************************"
echo " Bx Environment Setup Complete"
echo "****************************************"
