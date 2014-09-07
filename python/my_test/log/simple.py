import logging
import module_a
# Log everything, and send it to stderr.
logging.basicConfig(level=logging.DEBUG, 
    filename='picture_sudoku.log', filemode='w',  format='%(levelname)s: %(message)s')

# logging.basicConfig(filename='example.log',level=logging.DEBUG)

# everytime use a new file
# logging.basicConfig(filename='example.log', filemode='w', level=logging.DEBUG)

# 
# logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

# time
# logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

def g():
    1/0

def f():
    logging.debug("Inside f!")
    logging.warning('%s before you %s', 'Look', 'leap!')
    try:
        g()
    except Exception, ex:
        logging.exception("Something awful happened!")

    module_a.test_m()
    logging.debug("Finishing f!")

if __name__ == "__main__":
    f()