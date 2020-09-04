#!/bin/bash
source ./../env/bin/activate
gunicorn -c '../etc/gunicorn_hello_config.py' hello:application
deactivate
