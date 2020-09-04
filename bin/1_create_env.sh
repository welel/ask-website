#!/bin/bash
virtualenv -p /usr/bin/python3.4 env
source ./../env/bin/activate
pip install gunicorn
pip install django==2.0
pip install mysqlclient
deactivate
