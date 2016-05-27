import logging
import logging.handlers
import module_a
# Log everything, and send it to stderr.
# logging.basicConfig(level=logging.DEBUG, 
#     filename='picture_sudoku.log', filemode='w',
#     format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')#,  format='%(levelname)s: %(message)s')

# logging.basicConfig(filename='example.log',level=logging.DEBUG)

# everytime use a new file
# logging.basicConfig(filename='example.log', filemode='w', level=logging.DEBUG)

# 
# logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

# time
# logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

LOG_FILENAME = 'picture_sudoku.log'

# Set up a specific logger with our desired output level
my_logger = logging.getLogger('agentlogger')

# Add the log message handler to the logger
handler = logging.handlers.RotatingFileHandler(LOG_FILENAME, maxBytes=2000, backupCount=10)

# create a logging format
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

my_logger.addHandler(handler)

def g():
    1/0

def f():
    my_logger.debug("Inside f!")
    my_logger.warning('%s before you %s', 'Look', 'leap!')
    try:
        g()
    except Exception, ex:
        my_logger.exception("Something awful happened!")

    module_a.test_m()
    my_logger.debug("Finishing f!")

if __name__ == "__main__":
    f()