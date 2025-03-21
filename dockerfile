# Use Python 3.9
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy and install dependencies
COPY requirments.txt .
RUN pip install --no-cache-dir -r requirments.txt

# Copy the app files
COPY . . 

# Run Flask
CMD ["python", "main.py"]
