#!/bin/bash

exec sudo apt-get update
exec sudo pt-get install -f python3.5
exec sudo curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"
exec sudo python3.5 get-pip.py
exec sudo pip install django
exec sudo pip install gunicorn
