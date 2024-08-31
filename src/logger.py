import logging
import os
from datetime import datetime

## log file name should be based on date and time
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(),"logs")             ## path_to_cwd/logs/02_04_24_32_12_32.log
os.makedirs(logs_path, exist_ok=True)


LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format = "[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s" ,
    level=logging.INFO,

)

# if __name__=="__main__":
#     logging.info("logging has started")