my_list = ['a', 'b', 'c']
data = [ (1, 2), (3, 4), (5, 6), (7, 8) ]

if __name__ == '__main__':
    from minitest import *

    with test(enumerate):
        [(index, value) for index, value 
                in enumerate(my_list)].must_equal(
                [(0, 'a'), (1, 'b'), (2, 'c')])
        [(index, value) for index, value 
                in enumerate(my_list,1)].must_equal(
                [(1, 'a'), (2, 'b'), (3, 'c')])  

        [(index,x,y) for index, (x,y) in enumerate(data)].must_equal(
                [(0, 1, 2), (1, 3, 4), (2, 5, 6), (3, 7, 8)])