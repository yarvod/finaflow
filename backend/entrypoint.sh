#! /bin/bash

if [ "$1" = "run_django" ]; then
  python manage.py makemigrations jet
  python manage.py migrate
  apt-get install jpegoptim
  python manage.py collectstatic --no-input
  exec gunicorn backend_app.wsgi:application -b 0.0.0.0:8000 --reload --timeout 90 --workers 3
fi

if [ "$1" = "run_celery" ]; then
  python manage.py migrate
  exec celery -A backend_app worker -l info
fi

exec "$@"