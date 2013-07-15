import ctypes as c


class PyObject_HEAD(c.Structure):
    _fields_ = [
        ('HEAD', c.c_ubyte * (object.__basicsize__ -
                              c.sizeof(c.c_void_p))),
        ('ob_type', c.c_void_p)
    ]

_get_dict = c.pythonapi._PyObject_GetDictPtr
_get_dict.restype = c.POINTER(c.py_object)
_get_dict.argtypes = [c.py_object]

def get_dict(object):
    return _get_dict(object).contents.value

def my_method(self):
    print 'tada'
get_dict(str)['my_method'] = my_method

print ''.my_method()


def must_equal(self,other):
    print "other",other

get_dict(object)['must_equal'] = must_equal

obj = object()
obj.must_equal("234")