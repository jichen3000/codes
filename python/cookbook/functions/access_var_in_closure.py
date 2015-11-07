# nonlocal is only for python3
# def sample(): 
#     n=0
#     # Closure function
#     def func(): 
#         print('n=', n)
#     # Accessor methods for n
#     def get_n(): 
#         return n
#     def set_n(value): 
#         nonlocal n
#         n = value
#     # Attach as function attributes
#     func.get_n = get_n 
#     func.set_n = set_n 
#     return func
def sample(): 
    # Closure function
    def func(): 
        print('n=', func.n)
    # Accessor methods for n
    def get_n(): 
        return func.n
    def set_n(value): 
        func.n = value
    # Attach as function attributes
    func.n = 0
    func.get_n = get_n 
    func.set_n = set_n 
    return func    

if __name__ == '__main__':
    from minitest import *

    with test(sample):
        the_func = sample()
        the_func.get_n().must_equal(0)
        the_func.set_n(3)
        the_func.get_n().must_equal(3)