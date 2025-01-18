#!/bin/bash

# Ensure the Docker daemon is running
if ! systemctl is-active --quiet docker; then
    echo "Starting Docker..."
    sudo systemctl start docker
fi

# Build the Docker image
echo "Building the Docker image..."
sudo docker build -t searcs .

# Run the Docker container
echo "Running the Docker container..."
sudo docker run -d -p 5000:5000 --name searchview searchview

# Output the status
echo "Search engine is running at http://localhost:5000"
