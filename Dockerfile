# Use an official lightweight Python image as the base.
FROM python:3.12-slim

# Prevent Python from writing .pyc files and make console
# output appear immediately in Docker logs.
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory inside the container.
WORKDIR /app

# Copy only the dependency list into the image.
# The Django source code itself will be mounted with
# Docker Compose as required by the assignment.
COPY requirements.txt /app/

# Install the Python packages required by the application.
RUN pip install --no-cache-dir -r requirements.txt

# Django will listen on port 8000.
EXPOSE 8000

# Start Django and allow connections from outside the container.
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]