# Use a Python base image
FROM python:3.9

# Copy the requirements file to the container
COPY requirements.txt .

# Install the project dependencies
RUN pip install -r requirements.txt

# Copy the rest of the project files to the container
COPY . .

# Run the Celery worker command
CMD celery -A core worker -l INFO -B