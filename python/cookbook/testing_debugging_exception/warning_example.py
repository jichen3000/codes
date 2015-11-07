import warnings

def get_warning(x, logfile=None):
    if logfile is not None:
        print "logfile"
        warnings.warn('logfile argument deprecated', DeprecationWarning)
    return x


if __name__ == '__main__':
    from minitest import *

    with test(get_warning):
        get_warning(3, logfile=[])