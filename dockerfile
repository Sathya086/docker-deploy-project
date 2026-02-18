FROM python:3.12-slim

WORKDIR /usr/src/app

<<<<<<< HEAD
# Copy the Python app into the container 
=======
# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
>>>>>>> b0187715b9db5cef85b11f28a1e77d9c4cfd582b
COPY pythonapp.py .

# Run app
CMD ["python", "pythonapp.py"]
