# Use the Python base image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    gcc \
    default-libmysqlclient-dev \
    pkg-config && \
    rm -rf /var/lib/apt/lists/*

# Copy requirements.txt
COPY ./SMSProxyGateway/requirements.txt /app/requirements.txt

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r /app/requirements.txt

# Copy the rest of your application code
COPY ./SMSProxyGateway /app

# Specify the command to run on container start
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]