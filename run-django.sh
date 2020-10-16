#!/bin/sh

cd /code

python manage.py migrate --settings=proj.settings_production
python manage.py runserver 0.0.0.0:8000 --settings=proj.settings_production