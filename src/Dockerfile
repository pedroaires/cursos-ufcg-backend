# Use an official Python runtime as a base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /

# Copy the requirements file into the container
COPY requirements.txt .

# Install any dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app folder into the container
COPY app /app

# Copy the .env file into the container if needed
COPY .env .env

# Set the PYTHONPATH to include the /app directory
ENV PYTHONPATH=/app

# Expose port 5000 to the outside world
EXPOSE 5000

# Command to run the FastAPI application using uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5000"]
