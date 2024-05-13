import logging
from flask import Flask

app = Flask(__name__)

# Configure logging to send logs to a file
logging.basicConfig(filename='/var/log/logs.txt', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')
@app.route('/')
def hello_world():
    # Log a message
    logging.info('API endpoint accessed.')
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)