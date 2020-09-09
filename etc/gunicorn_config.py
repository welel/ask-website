from os import getenv
from dotenv import load_dotenv


load_dotenv()
pythonpath = getenv('PWD') + '/../ask'
bind = '0.0.0.0:8000'
raw_env = 'DJANGO_SETTINGS_MODULE=ask.settings'
