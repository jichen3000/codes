import traceback


def wrap_exceptions(the_func):
    def intern_func(*args, **kws):
        try:
            the_func(*args, **kws)
        except Exception, e:
            return "get it"
            # print "get it"
            # print traceback.format_exc()
    return intern_func

def wrap_exceptions_with_code(the_code):
    def wrap_exceptions(the_func):
        def intern_func(*args, **kws):
            try:
                the_func(*args, **kws)
            except Exception, e:
                return "get it" + str(the_code)
                # print "get it"
                # print traceback.format_exc()
        return intern_func
    return wrap_exceptions

class MyException(Exception):
    """My exception"""

def wrap_my_exceptions_with_code(the_code):
    def wrap_exceptions(the_func):
        def intern_func(*args, **kws):
            try:
                the_func(*args, **kws)
            except MyException, mye:
                return "{0} : my exception is: {1}".format(str(the_code), mye.message)
            except Exception, e:
                return "get it" + str(the_code)
                # print "get it"
                # print traceback.format_exc()
        return intern_func
    return wrap_exceptions


@wrap_exceptions
def div_zero(the_num):
    the_num/0

@wrap_exceptions
def raise_something(msg1, msg2):
    raise Exception("{0}, {1}".format(msg1, msg2))

@wrap_exceptions_with_code(3)
def raise_with_code(msg1, msg2):
    raise Exception("{0}, {1}".format(msg1, msg2))

@wrap_my_exceptions_with_code(3)
def raise_my_exception_with_code(msg1, msg2):
    raise MyException("{0}, {1}".format(msg1, msg2))

@wrap_my_exceptions_with_code(3)
def div_zero2(the_num):
    the_num/0

if __name__ == '__main__':
    from minitest import *

    with test(div_zero):
        div_zero(2).must_equal("get it")

    with test(wrap_exceptions):
        raise_something("jc","colin").must_equal("get it")

    with test(wrap_exceptions_with_code):
        raise_with_code("jc","colin").must_equal("get it3")        

    with test(wrap_my_exceptions_with_code):
        raise_my_exception_with_code("jc","colin").must_equal("3 : my exception is: jc, colin")         
        div_zero2(10).must_equal("get it3")          