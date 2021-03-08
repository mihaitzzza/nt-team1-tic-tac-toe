import game
from game.loggers import get_logger

logger = get_logger(__name__)

if __name__ == '__main__':
    try:
        game.start()
    except BaseException as e:
        logger.exception(e)
