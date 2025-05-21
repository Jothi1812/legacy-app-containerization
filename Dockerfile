# # Use an official Python runtime as a base image
# FROM python:3.9-slim

# # Set the working directory in the container
# WORKDIR /app

# # Copy the application files into the container
# COPY ./app /app

# # Install any necessary dependencies (if needed)
# # RUN pip install --no-cache-dir -r requirements.txt

# # Command to run the application
# CMD ["python", "app.py"]


# # Use an official Python runtime as a parent image
# FROM python:3.9-slim

# # Set the working directory in the container
# WORKDIR /app

# # Copy the current directory contents into the container at /app
# COPY . /app

# # Install any needed dependencies
# RUN pip install --no-cache-dir -r requirements.txt

# # Make port 5000 available to the world outside this container
# EXPOSE 5000

# # Define environment variable
# ENV NAME World

# # Run app.py when the container launches
# CMD ["python", "app.py"]

FROM python:3.8

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    default-libmysqlclient-dev \
    pkg-config && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

CMD ["python", "app.py"]