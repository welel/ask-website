#!/bin/bash
source ./../env/bin/activate
gunicorn -c '../ask/gunicorn_ask_config.py' ask.wsgi
deactivate
