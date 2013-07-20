class Person(object):
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def __init__(self, name, age):
        self.name = name
        self.age = age

def print_method_info_decorator(func):
    '''This decorator dumps out the arguments passed to a function before calling it'''
    argnames = func.func_code.co_varnames[:func.func_code.co_argcount]
    fname = func.func_name
    def print_info_func(*args,**kwargs):
        print fname, "(", ', '.join(
            '%s=%r' % entry
            for entry in zip(argnames,
                args[:len(argnames)])+
            [("args",list(args[len(argnames):]))]+[("kwargs",kwargs)]) +")"
        return func(*args, **kwargs)
        
    return print_info_func

def add_decorators_for_all_methods_in_class(clazz, decorator):
    ''' not work for built in function, like m2.ssl_ctx_free'''
    self_methods = filter(lambda name: not name.startswith('__'),
        clazz.__dict__.keys())
    def set_method(name):
        wrapped_method = print_method_info_decorator(clazz.__dict__[name])
        setattr(clazz,name, wrapped_method)
        return wrapped_method
        # clazz[name] = \
        #     print_method_info_decorator(clazz.__dict__[name])
        # return clazz.__dict__[name]
    map(set_method, self_methods)
    # [set_method(name) for name in self_methods]

if __name__ == '__main__':
    add_decorators_for_all_methods_in_class(
        Person, print_method_info_decorator)
    colin = Person("colin", 22)
    print colin.get_name()
