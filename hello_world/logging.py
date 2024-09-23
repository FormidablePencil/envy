import logging

# Configure logging
logging.basicConfig(filename='websocket_logs.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

# Function to log messages

def log_message(message):
    logging.info(message)