# Use the official Python image from the Docker Hub
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the required Python packages
RUN pip install Flask googlesearch-python

# Make sure to install any related dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV FLASK_APP=search.py

# Run the application
CMD ["flask", "run", "--host=0.0.0.0"]
