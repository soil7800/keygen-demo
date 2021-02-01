#!/bin/sh

# Collect static files
echo "Collect static files"
python manage.py collectstatic --noinput

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate

# Start supervisord
echo "Start supervisord"
supervisord


echo "Run daphne"
daphne -b 0.0.0.0 -p 8000 keygen.asgi:application