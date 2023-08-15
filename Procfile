web: gunicorn core.wsgi --log-file -
worker: celery -A core.celery -l info -c 4