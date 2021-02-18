import game
from game.loggers import logger, file_logger

if __name__ == '__main__':
    try:
        game.start()
    except BaseException as e:
        logger.exception(e)
