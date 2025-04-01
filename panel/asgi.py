"""
ASGI config for a panel project.

It exposes the ASGI callable as a module-level variable named application.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

from decouple import config

debug_mode = config('DEBUG', cast=bool)

if debug_mode:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'panel.envs.development')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'panel.envs.production')

application = get_asgi_application()
