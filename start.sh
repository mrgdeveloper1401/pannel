#!/bin/sh

python manage.py collectstatic --noinput
gunicorn panel.wsgi -b 0.0.0.0:8000
