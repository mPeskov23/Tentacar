#!/bin/bash
python3 -m venv venv --system-site-packages
source venv/bin/activate
pip install -r requirements.txt
cd ./firmware
python3 main.py