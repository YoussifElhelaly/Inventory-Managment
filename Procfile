web: web: gunicorn core.wsgi --timeout 120 --workers=3  & celery -A core worker --loglevel=INFO --pool=solo & celery -A core beat -l INFO
