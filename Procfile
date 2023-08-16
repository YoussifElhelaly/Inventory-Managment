web: web: gunicorn core.wsgi --timeout 120 --workers=3 --threads=3 --worker-connections=1000 & celery -A core worker --loglevel=INFO --pool=solo & celery -A core beat -l INFO
