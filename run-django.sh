#!/bin/sh

cd /code

until python test_database.py; do
  echo "Database is unavailable - sleeping"
  sleep 1
done

python manage.py migrate --settings=proj.settings_production
python manage.py collectstatic --no-input
#python manage.py runserver 0.0.0.0:8000 --settings=proj.settings_production
gunicorn proj.wsgi:application --env DJANGO_SETTINGS_MODULE=proj.settings_production --limit-request-line 0 --timeout 600 -w 4 -b :8000