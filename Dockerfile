# Use the Python 3.8 slim version as the base image
FROM python:3.8-slim-buster

# Update package lists and install AWS CLI
RUN apt update -y && apt install awscli -y

# Set the working directory inside the container to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install Python dependencies from requirements.txt
RUN pip install -r requirements.txt

# Expose port 8080 to allow external connections
EXPOSE 8080

# Specify the command to run the application when the container starts
CMD [ "python", "app.py" ]