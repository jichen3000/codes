def print_method_info(func):
    '''This decorator dumps out the arguments passed to a function before calling it'''
    argnames = func.func_code.co_varnames[:func.func_code.co_argcount]
    fname = func.func_name
    def echo_func(*args,**kwargs):
        print fname, "(", ', '.join(
            '%s=%r' % entry
            for entry in zip(argnames,args[:len(argnames)])+[("args",list(args[len(argnames):]))]+[("kwargs",kwargs)]) +")"
    return echo_func

@print_method_info
def test_me(a, b = 4, c = 'blah-blah', *args, **kwargs):
    pass


if __name__ == '__main__':
    from minitest import *

    @print_method_info
    with test('123'):
        print "in with"
        
    with test(test_me):
        test_me(1, 2, 3, 4, 5, d = 6, g = 12.9)
