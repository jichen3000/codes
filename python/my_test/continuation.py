def foo(x,contiuation):
    contiuation(x+1,contiuation)

def pp(x):
    return x*x

print foo(1,foo)