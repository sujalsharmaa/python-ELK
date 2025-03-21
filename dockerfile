# Dockerfile
FROM python:3.9

COPY . .
RUN pip install -r requirments.txt

COPY . .
CMD ["python", "app.py"]
