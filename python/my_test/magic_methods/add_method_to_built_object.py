import ctypes


# class PyObject_HEAD(ctypes.Structure):
#     _fields_ = [
#         ('HEAD', ctypes.c_ubyte * (object.__basicsize__ -
#                               ctypes.sizeof(ctypes.c_void_p))),
#         ('ob_type', ctypes.c_void_p)
#     ]

_get_dict = ctypes.pythonapi._PyObject_GetDictPtr
_get_dict.restype = ctypes.POINTER(ctypes.py_object)
_get_dict.argtypes = [ctypes.py_object]

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