#!/bin/bash
source ./../env/bin/activate
gunicorn -c '../etc/gunicorn_config.py' ask.wsgi
deactivate
