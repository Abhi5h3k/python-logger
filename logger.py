"""
Author : Abhishek
Date   : 4/17/2023

"""

import logging
import sys
import os
from datetime import datetime, timedelta
import pathlib

# Create a logger object
log = logging.getLogger(__name__)

# Set the logging level to capture
log.setLevel(logging.INFO)

# Folder path to save log
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
base_folder = "logs"

# Define the log file path and name with timestamp
log_path = os.path.join(BASE_DIR, f"{base_folder}")
# create folder
pathlib.Path(log_path).mkdir(parents=True, exist_ok=True)

log_filename = datetime.now().strftime("%Y-%m-%d") + ".log"
log_file = os.path.join(log_path, log_filename)

# Configure the file handler to write log messages to the file
file_handler = logging.FileHandler(log_file, mode="a+")

# Set the formatter for the log messages to include the timestamp and other details
formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(module)s -> %(funcName)s -> %(lineno)d :\n%(message)s\n",
    datefmt="%Y-%m-%d %H:%M:%S",
)
file_handler.setFormatter(formatter)

# Add the file handler to the logger
log.addHandler(file_handler)

# Define a function to handle unhandled exceptions
def handle_exception(exc_type, exc_value, exc_traceback):
    if issubclass(exc_type, KeyboardInterrupt):
        # If the exception is a KeyboardInterrupt, let Python handle it normally
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return

    # Log the exception message and traceback to the file
    log.error(
        "Unhandled exception occurred:", exc_info=(exc_type, exc_value, exc_traceback)
    )


# Set the excepthook to use the handle_exception function
sys.excepthook = handle_exception

# Delete log files older than 7 days
for filename in os.listdir(log_path):
    file_path = os.path.join(log_path, filename)
    if os.stat(file_path).st_mtime < (datetime.now() - timedelta(days=7)).timestamp():
        os.remove(file_path)