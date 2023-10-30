#!/bin/sh

sleep 4

python manage.py migrate
# python manage.py create_default_admin
# python manage.py loaddata questions/fixtures/questions.json

exec "$@"
