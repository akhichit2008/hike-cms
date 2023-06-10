'''
Holds configs for the application
'''

import os
from dotenv import load_dotenv

class Config(object):
    load_dotenv()
    SECRET_KEY = os.environ['APP_SECRET_KEY']
