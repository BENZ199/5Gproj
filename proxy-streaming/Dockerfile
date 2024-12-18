# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /usr/src/app

# Copy the TCP proxy script into the container
COPY tcp_proxy.py .

# Install any necessary dependencies (if needed)
# For now, we don't need any extra dependencies

# Expose the port the proxy will listen on
EXPOSE 7654

# Run the TCP proxy when the container starts
CMD ["python", "./tcp_proxy.py"]
