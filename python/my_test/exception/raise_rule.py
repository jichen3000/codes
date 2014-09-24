
import sys

class MyError(Exception):
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
            error_block = '''Traceback (most recent call last):
  File "/Users/colin/work/codes/python/my_test/exception/extend_exception.py", line 35, in <module>
    raise_key_error_with_original_info()
  File "/Users/colin/work/codes/python/my_test/exception/extend_exception.py", line 14, in raise_key_error_with_original_info
    the_dict['mm']
MyError: 'mm'
'''
            traceback.format_exc().must_equal(error_block)

    with test(raise_key_error_without_original_info):
        try:
            raise_key_error_without_original_info()
        except Exception, e:
            error_block = '''Traceback (most recent call last):
  File "/Users/colin/work/codes/python/my_test/exception/extend_exception.py", line 48, in <module>
    raise_key_error_without_original_info()
  File "/Users/colin/work/codes/python/my_test/exception/extend_exception.py", line 24, in raise_key_error_without_original_info
    raise MyError(e)
MyError: 'mm'
'''
            traceback.format_exc().must_equal(error_block)
            # traceback.format_exc().p()
            # print e.__class__
            # print e.__class__.__bases__

