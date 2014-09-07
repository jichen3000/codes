import logging


LOGGER = logging.getLogger(__name__)


if __name__ == '__main__':
    
    logging.basicConfig(level=logging.DEBUG)
    LOGGER.info("123")