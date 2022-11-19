#!/bin/bash
echo "****************************************"
echo " Setting up bx Environment"
echo "****************************************"

echo "Updating package manager..."
sudo add-apt-repository -y ppa:deadsnakes/ppa

echo "Installing Python 3.8 and Virtual Environment"
sudo apt-get update
sudo DEBIAN_FRONTEND=noninteractive apt-get install -y python3.8.13

echo "Making Python 3.8 the default..."
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.10 1
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.8.13 2

echo "Checking the Python version..."
python3 --version

echo "Installing Python depenencies..."
source .bxenv/bin/activate && python3 -m pip install --upgrade pip wheel
source .bxenv/bin/activate && pip install -r ./brandxpert/requirements.txt

echo "****************************************"
echo " Bx Environment Setup Complete"
echo "****************************************"
echo ""
echo "Use 'exit' to close this terminal and open a new one to initialize the environment"
echo ""