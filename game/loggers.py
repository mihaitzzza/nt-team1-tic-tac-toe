import logging
import sys
import os
import uuid


log_level = logging.DEBUG
log_format = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s: %(message)s', '%Y-%m-%d %H:%M:%S')
log_file = os.path.join('games_history', f'{uuid.uuid4()}.txt')
stdout_handler = logging.StreamHandler(sys.stdout)


def get_logger(module_name=__name__):
    # use logger.info instead of print statements
    # will print to console and add to log file at the same time
    logger = logging.getLogger(module_name)
    logger.addHandler(stdout_handler)
    logger.setLevel(log_level)

    file_log_output = logging.FileHandler(log_file)
    file_log_output.setFormatter(log_format)
    logger.addHandler(file_log_output)

    return logger
