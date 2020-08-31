#command = '/home/pavel/web/env/bin/gunicorn'
command = '/home/box/web/env/bin/gunicorn'

#pythonpath = '/home/pavel/web/ask'
pythonpath = '/home/box/web/ask'

bind = '0.0.0.0:8000'
raw_env = 'DJANGO_SETTINGS_MODULE=ask.settings'
