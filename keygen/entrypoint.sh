#!/bin/sh

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate

# Start supervisord
echo "Start supervisord"
supervisord


echo "Run daphne"
python manage.py runserver