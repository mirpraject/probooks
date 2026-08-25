#!/bin/bash
echo "Running collectstatic..."
python manage.py collectstatic --noinput

echo "Running migrations..."
python manage.py migrate

echo "Starting server..."
daphne -b 0.0.0.0 -p $PORT config.asgi:application
