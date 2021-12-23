#!/bin/bash

while ! nc -z db_host 5432; do
    sleep 0.1
done

echo "PostgreSQL started"

python manage.py run -p 8000
