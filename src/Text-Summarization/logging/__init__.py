import os 
import sys 
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s] %(message)s"
log_dir = "logs"
log_filepath = os.path.join(log_dir, "text_summarization.log")
os.makedirs(log_dir, exist_ok=True)


logging.basicConfig(filename=log_filepath,
                    level=logging.INFO,
                    format=logging_str,


                    handlers=[
                        logging.StreamHandler(sys.stdout),
                        logging.FileHandler(log_filepath)
                    ]
                    )
logger = logging.getLogger("text_summarizationLogger")