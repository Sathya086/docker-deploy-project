# Use the official Python base image1
FROM python:3.12-slim

# Set working directory inside the container
WORKDIR /usr/src/app

# Copy the Python app into the container
COPY pythonapp.py .

# (Optional) Install any Python dependencies if needed
# RUN pip install --no-cache-dir -r requirements.txt

# Set default command to run the app
CMD ["python", "pythonapp"]
