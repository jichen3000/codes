if __name__ == '__main__':
    from minitest import *

    with test("align"):
        text = 'Hello World'
        text.ljust(20).must_equal('Hello World         ')
        text.rjust(20,"=").must_equal('=========Hello World')
        text.center(20,"*").must_equal('****Hello World*****')
        format(text, '>20').must_equal('         Hello World')
        format(text, '<20').must_equal('Hello World         ')
        format(text, '^20').must_equal('    Hello World     ')
        format(text, '*^20').must_equal('****Hello World*****')
        '{:>10s} {:>10s}'.format('Hello', 'World').must_equal('     Hello      World')
        #One benefit of format() is that it is not specific to strings. It works with any value
        x=1.2345
        format(x, '^10.2f')
        pass