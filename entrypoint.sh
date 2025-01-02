#!/bin/bash

set -e

echo "Ejecutando migraciones..."
pipenv run python soulmirror/manage.py migrate

echo "Iniciando servidor de desarrollo en 0.0.0.0:8000..."
pipenv run python soulmirror/manage.py runserver 0.0.0.0:8000
