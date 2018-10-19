import sub.get_file_here as gf

if __name__ == '__main__':
    from minitest import *

    with test("test file"):
        gf.get_file()