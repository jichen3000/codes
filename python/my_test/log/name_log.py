import logging


LOGGER = logging.getLogger(__name__)


if __name__ == '__main__':

    logging.basicConfig(level=logging.DEBUG)
    # logging.basicConfig(filename='example.log', filemode='w', level=logging.DEBUG)
    LOGGER.info("123")
    import module_a
    module_a.test_m()
