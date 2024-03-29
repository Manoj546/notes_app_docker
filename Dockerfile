# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY app.py .
COPY Model ./Model
COPY static ./static
COPY templates ./templates
COPY .env .
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install Flask flask_pymongo python-dotenv

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV FLASK_APP=app.py

# Run app.py when the container launches
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]