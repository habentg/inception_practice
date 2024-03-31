
# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the dependencies
RUN pip install -r requirements.txt

# Copy the application code to the container
COPY . .

# Expose port 5000 for the application
EXPOSE 5000

# Run the command to start the application
CMD ["python", "app.py"]