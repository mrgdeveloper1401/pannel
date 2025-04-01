from panel.settings import *

ALLOWED_HOSTS = []

SECRET_KEY = config('SECRET_KEY', cast=str)

SIMPLE_JWT['SIGNING_KEY'] = SECRET_KEY
