def print_method_info(func):
    '''This decorator dumps out the arguments passed to a function before calling it'''
    argnames = func.func_code.co_varnames[:func.func_code.co_argcount]
    fname = func.func_name
    print '123'
    def echo_func(*args,**kwargs):
        print fname, "(", ', '.join(
            '%s=%r' % entry
            for entry in zip(argnames,args[:len(argnames)])+[("args",list(args[len(argnames):]))]+[("kwargs",kwargs)]) +")"
    return echo_func

@print_method_info
def test(a, b = 4, c = 'blah-blah', *args, **kwargs):
    print 'it in test '

test(1, 2, 3, 4, 5, d = 6, g = 12.9)
# print(dump_args.__doc__)

