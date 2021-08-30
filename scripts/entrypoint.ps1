/usr/local/bin/gunicorn Portfolio.wsgi:application --bind "0.0.0.0$PORT"  --env DJANGO_SETTINGS_MODULE=Portfolio.settings.production



