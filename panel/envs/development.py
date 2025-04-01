from panel.settings import *

from panel.settings import BASE_DIR

SECRET_KEY = 'django-insecure-@uj5__@5p9c8lp6%+a-wdhpb*ui_d8ey6xe(wmz*(uc33vk+jh'

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

SIMPLE_JWT['SIGNING_KEY'] = SECRET_KEY

INSTALLED_APPS += ('debug_toolbar', "rest_framework")

MIDDLEWARE += ('debug_toolbar.middleware.DebugToolbarMiddleware',)

INTERNAL_IPS = [
    "127.0.0.1"
]