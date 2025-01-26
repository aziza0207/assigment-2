#!/bin/sh

python manage.py flush --no-input
python manage.py migrate
python manage.py create_default_admin
python manage.py collectstatic --no-input --clear
gunicorn config.wsgi:application --bind 0.0.0.0:8000