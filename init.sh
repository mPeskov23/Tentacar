#!/bin/bash
source venv/bin/activate
pip3 install -r requirements.txt
cd ./firmware
python3 test.py