#!/bin/bash

# collect static files
# python manage.py collectstatic --noinput

# run database migrations
python manage.py makemigrations
python manage.py migrate

# run server
python manage.py runserver 0.0.0.0:8000