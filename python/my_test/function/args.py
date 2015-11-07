def foo(*args):
    print "in foo"
    print args

def bar(arg_1, *args):
    print "in bar"
    print arg_1
    print args

foo()
foo(1,2)
bar(1,2)
bar()