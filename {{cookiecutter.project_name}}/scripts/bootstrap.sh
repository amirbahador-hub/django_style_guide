#!/bin/bash

E_NO_POSTGRES_USERNAME=60

POSTGRES_USERNAME="$1"
DATABASE_NAME="{{cookiecutter.project_slug}}"

if [[ -z "$POSTGRES_USERNAME" ]]
then
  echo "Call `basename $0` with your postgres user as the first argument."
  exit "$E_NO_POSTGRES_USERNAME"
fi

dropdb --if-exists "$DATABASE_NAME"

sudo -U postgres createdb -O "$POSTGRES_USERNAME" "$DATABASE_NAME"

python manage.py migrate
