import logging
import sys
import os
import uuid


log_level = logging.DEBUG
log_file = os.path.join('games_history', f'{uuid.uuid4()}.txt')
log_format = '%(asctime)s - %(levelname)s - %(name)s: %(message)s'


# use logger.info instead of print statements
# will print to console and add to log file at the same time


logger = logging.getLogger('l %s' % __name__)
stdout_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(stdout_handler)
logger.setLevel(log_level)
file_log_output = logging.FileHandler(log_file)
logger.addHandler(file_log_output)


# use file_logger.info for what needs to be added
# to log file, but not printed in the console


file_logger = logging.getLogger(__name__)
file_logger.setLevel(log_level)
file_logger.addHandler(file_log_output)
