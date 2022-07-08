#!/bin/bash
APP_PORT=${PORT:-8000}
cd /sentir
gunicorn --worker-tmp-dir /dev/shm sentir.wsgi:application --bind "0.0.0.0:${APP_PORT}"