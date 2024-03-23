#!/bin/sh

if [ "$DEBUG" = "True" ];
then
    python lizetest/manage.py runserver 0.0.0.0:8000
else
    gunicorn --bind 0.0.0.0:8000 --workers=1 --threads=3 --timeout=300 --capture-output --log-level warning lizetest.wsgi:application
fi