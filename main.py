# app.py
from flask import Flask
import logging
import json
from datetime import datetime

app = Flask(__name__)

# Configure logging
log_file = "app.log"
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s',
    handlers=[logging.FileHandler(log_file), logging.StreamHandler()]
)

@app.route('/')
def hello():
    app.logger.info(json.dumps({"message": "Hello, World!", "timestamp": str(datetime.now())}))
    return "Hello, ELK Stack!"

@app.route('/error')
def error():
    app.logger.error(json.dumps({"message": "Something went wrong!", "timestamp": str(datetime.now())}))
    return "Error logged!", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
