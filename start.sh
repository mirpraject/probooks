#!/bin/bash
echo "Running collectstatic..."
python manage.py collectstatic --noinput

echo "Running migrations..."
python manage.py migrate

echo "Seeding initial data..."
python manage.py init_achievements
python manage.py seed_dev_data

echo "Starting server..."
daphne -b 0.0.0.0 -p ${PORT:-8080} config.asgi:application
