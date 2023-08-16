web: python manage.py migrate && python manage.py collectstatic --noinput && celery -A core worker --loglevel=INFO & gunicorn core.wsgi
