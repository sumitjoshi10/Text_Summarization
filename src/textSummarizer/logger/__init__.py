import logging
import os
import sys
from datetime import datetime

# from from_root import from_root

LOGGING_STR = "[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s"
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
LOG_DIR = "logs"

log_path = os.path.join(os.getcwd(),LOG_DIR)
os.makedirs(log_path,exist_ok=True)

LOG_FILE_PATH = os.path.join(log_path,LOG_FILE)

logging.basicConfig(
    level=logging.INFO,
    format=LOGGING_STR,
    

    handlers={
        logging.FileHandler(LOG_FILE_PATH),
        logging.StreamHandler(sys.stdout)
    }   
)

logger = logging.getLogger("TextSummarizerLogger")