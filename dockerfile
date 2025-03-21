# Dockerfile
FROM python:3.9

WORKDIR /app
COPY requirments.txt requirments.txt
RUN pip install -r requirements.txt

COPY . .
CMD ["python", "app.py"]
