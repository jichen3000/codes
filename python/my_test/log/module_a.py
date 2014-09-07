import logging

def test_m():
    logging.info("I'm in test_m")


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)

    test_m()