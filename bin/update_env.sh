#!bin/bash

exec apt-get update
exec pt-get install -f python3.5
exec curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"
exec python3.5 get-pip.py
exec pip install django
exec pip install gunicorn
