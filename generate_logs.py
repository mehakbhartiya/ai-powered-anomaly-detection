import random
from loguru import logger

#log types
log_types = ['INFO', 'ERROR', 'WARNING', 'DEBUG']

#Create the log file
logger.add("logs/app.log")

for _ in range(1000):
    log_type=random.choice(log_types)
    logger.log(log_type, f"Sample {log_type} message.")

