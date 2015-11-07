from itertools import izip_longest

if __name__ == '__main__':
    from minitest import *

    with test("zip dict"):
        headers = ['name', 'shares', 'price']
        values = ['ACME', 100, 490.1]
        dict(zip(headers,values)).must_equal(
                {'name': 'ACME', 'price': 490.1, 'shares': 100})

    with test(zip):
        a = [1, 2, 3]
        b = ['w', 'x', 'y', 'z'] 
        list(zip(a,b)).must_equal(
                [(1, 'w'), (2, 'x'), (3, 'y')])

        list(izip_longest(a,b)).must_equal(
                [(1, 'w'), (2, 'x'), (3, 'y'), (None, 'z')])

        list(izip_longest(a,b,fillvalue=99)).must_equal(
                [(1, 'w'), (2, 'x'), (3, 'y'), (99, 'z')])
