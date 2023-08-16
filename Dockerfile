# Use a Python base image
FROM python:3.9

WORKDIR /app

# Copy the project files to the container
COPY . .

# Install the project dependencies
RUN pip install --no-cache-dir -r requirements.txt

CMD celery -A core worker -l INFO --pool=prefork --concurrency=8 & python manage.py migrate && gunicorn core.wsgi --log-file -