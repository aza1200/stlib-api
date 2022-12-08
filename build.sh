#!/usr/bin/env bash
# exit on error
set -o errexit
pip install --upgrade pip
pip install psycopg2-binary

poetry install
pip install --force-reinstall -U setuptools
python manage.py collectstatic --no-input
python manage.py migrate