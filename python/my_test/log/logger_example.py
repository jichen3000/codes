# for the module file, just like the module_a.py
# for main file, just like this one

import logging


LOGGER = logging.getLogger(__name__)


if __name__ == '__main__':

    logging.basicConfig(level=logging.DEBUG)
    # formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    # LOGGER.setFormatter(formatter)
    # logging.basicConfig(filename='example.log', filemode='w', level=logging.DEBUG)
    LOGGER.info("123")
    import module_a
    module_a.test_m()
