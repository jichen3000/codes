import logging

LOGGER = logging.getLogger(__name__)
def test_m():
    LOGGER.info("I'm in test_m")


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)

    test_m()