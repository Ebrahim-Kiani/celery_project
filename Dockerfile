FROM python:3.12.4-alpine3.20

# Create a new user
RUN adduser -D -h /home/django-user django-user

WORKDIR /app
RUN chown -R django-user:django-user /app

# Switch to the new user
USER django-user

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PATH="/home/django-user/.local/bin:$PATH"



# Install dependencies
RUN pip install --upgrade pip
COPY ./req.txt /app/req.txt
RUN pip install --no-cache-dir -r /app/req.txt

# Install Celery

# Copy your application code
COPY --chown=django-user:django-user . /app

# Set the working directory to the app directory
WORKDIR /app

# Define the command to start Celery
CMD celery -A celery_project.celery flower --loglevel=info