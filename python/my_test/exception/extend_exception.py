
import sys

class MyError(Exception):
    def __init__(self, the_exception=None):
        super(MyError,self).__init__(the_exception)
        if the_exception:
            self.real_exception = the_exception
        pass
    pass


def raise_key_error_with_original_info():
    ''' It will always give the origianl line the_dict['mm'].
        When coding, I should follow this way.
    '''
    the_dict = {}
    try:
        the_dict['mm']
    except KeyError, e:
        # raise MyError(e)
        raise MyError(e), None, sys.exc_info()[2]

def raise_key_error_without_original_info():
    the_dict = {}
    try:
        the_dict['mm']
    except KeyError, e:
        raise MyError(e)
        # raise MyError(e), None, sys.exc_info()[2]


if __name__ == '__main__':
    from minitest import *

    import traceback

    with test(raise_key_error_with_original_info):
        try:
            raise_key_error_with_original_info()
        except Exception, e:
            traceback.format_exc().p()
            print e.__class__
            print e.__class__.__bases__
            pass

    with test(raise_key_error_without_original_info):
        try:
            raise_key_error_without_original_info()
        except Exception, e:
            traceback.format_exc().p()
            print e.__class__
            print e.__class__.__bases__

        raise_key_error_with_original_info()
