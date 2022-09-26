import os
from datetime import datetime
import logging

# Variable declaration for logging.basicConfig()
LOG_DIR = "wheat_logs"
CURRENT_TIME_STAMP = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}"
LOG_FILE_NAME = f"log_{CURRENT_TIME_STAMP}.log"
LOG_FILE_PATH = os.path.join(LOG_DIR,LOG_FILE_NAME)
LOG_FORMAT = '[%(asctime)s] - %(name)s -  %(levelname)s - %(lineno)d - [%(filename)s - %(funcName)s()] - %(message)s'
LOG_LEVEL = logging.INFO

# Creatre logging directiory
os.makedirs(LOG_DIR, exist_ok=True)

# Create log file
logging.basicConfig(filename=LOG_FILE_PATH,
                    filemode="w",
                    format=LOG_FORMAT,
                    level=LOG_LEVEL)