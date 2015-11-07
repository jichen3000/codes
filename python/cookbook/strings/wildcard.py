from fnmatch import fnmatch, fnmatchcase

if __name__ == '__main__':
    from minitest import *

    with test(fnmatch):
        fnmatch('foo.txt', '?oo.txt').must_equal(True)
        fnmatch('Dat45.csv', 'Dat[0-9]*').must_equal(True)
        # case-sensitivity which varies based on operating system
        # not depond on this
        # for mac
        fnmatch('foo.txt', '*.TXT').must_equal(False)

        # using case-sensitivity
        fnmatchcase('foo.txt', '*.TXT').must_equal(False)