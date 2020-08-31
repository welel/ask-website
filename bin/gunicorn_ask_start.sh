#!/bin/bash

# source /home/pavel/web/env/bin/activate
source /home/box/web/env/bin/activate

#exec gunicorn -c '/home/pavel/web/ask/gunicorn_ask_config.py' ask.wsgi
exec gunicorn -c '/home/box/web/ask/gunicorn_ask_config.py' ask.wsgi
