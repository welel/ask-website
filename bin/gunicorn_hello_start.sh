#!/bin/bash

# Gunicorn server for hello application
exec gunicorn -c '../etc/gunicorn_hello_config.py' hello:application
