import ctypes

VERSION = '0.0.1'

def get_dict(object):
    _get_dict = ctypes.pythonapi._PyObject_GetDictPtr
    _get_dict.restype = ctypes.POINTER(ctypes.py_object)
    _get_dict.argtypes = [ctypes.py_object]
    return _get_dict(object).contents.value

def set_method_to_builtin(clazz, method_fun, method_name=None):
    method_name = method_name or method_fun.func_code.co_name
    get_dict(clazz)[method_name] = method_fun

def set_method_to_object(method_fun, method_name=None):
    set_method_to_builtin(object, method_fun, method_name)

def must_equal(self, other):
    assert self == other
    return self

def must_equal_with_func(self, other, fun):
    assert fun(self, other)
    return self

def must_true(self):
    assert self
    return self

def p(self):
    print self
    return self

from pprint import pprint
def pp(self):
    pprint(self)
    return self

def inject_musts_methods():
    [set_method_to_object(fun) for name, fun 
        in globals().iteritems() 
        if name.startswith('must_')]
    set_method_to_object(p)
    set_method_to_object(pp)


inject_musts_methods()

