import os
import logging
from datetime import datetime

# Create a unique log file name based on the current date and time.
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M')}.log"

# Define the log file's path using the current working directory and a 'logs' subdirectory.
log_path = os.path.join(os.getcwd(), "logs", LOG_FILE)

# Ensure that the directory structure for logs exists. If not, create it.
os.makedirs(log_path, exist_ok=True)

# Create the full path to the log file.
LOG_FILE_PATH = os.path.join(log_path, LOG_FILE)

# Configure the logging system.
logging.basicConfig(
    filename=LOG_FILE_PATH,  # Specify the log file where log messages will be written.
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",  # Define the log message format.
    level=logging.INFO  # Set the logging level to INFO, which captures messages with INFO level or higher.
)
