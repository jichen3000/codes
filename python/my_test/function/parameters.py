def with_kwargs(**kwargs):
    print type(kwargs)
    for k,v in kwargs.items():
        (k,v).p()

if __name__ == '__main__':
    from minitest import *

    with test(with_kwargs):
        with_kwargs(a=1,c=3,b=2,c1=4,mm=5)
    
    