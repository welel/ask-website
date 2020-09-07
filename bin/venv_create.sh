#!/bin/bash
virtualenv ../env
source ./../env/bin/activate
pip install gunicorn
pip install Django
pip install mysqlclient
pip install -U python-dotenv
deactivate
