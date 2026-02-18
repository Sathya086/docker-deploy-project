FROM python:3.12-slim

WORKDIR /usr/src/app

# Install dependencies 
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY pythonapp.py .

# Run app
CMD ["python", "pythonapp.py"]
