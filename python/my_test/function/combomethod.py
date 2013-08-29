class combomethod(object):
    ''' it will give a class a instance method as well as a class method,
        and will invoke the instance method firstly.
        From stackoverflow.
    '''
    def __init__(self, method):
        self.method = method

    def __get__(self, obj=None, objtype=None):
        @functools.wraps(self.method)
        def _wrapper(*args, **kwargs):
            if obj is not None:
                return self.method(obj, *args, **kwargs)
            else:
                return self.method(objtype, *args, **kwargs)
        return _wrapper
