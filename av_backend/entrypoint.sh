#!/usr/bin/env bash

set -xe

python manage.py migrate --noinput
gunicorn --config=gunicorn.conf.py
