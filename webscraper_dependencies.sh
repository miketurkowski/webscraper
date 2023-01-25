#!/bin/bash

# updates apt package index
sudo apt-get update

# installs python3 & pip3
sudo apt-get install -y python3 python3-pip 

# installs the required libraries
pip3 install requests beautifulsoup4 urllib3



