from last_function import *

def last_two():
    print "last_two"

if __name__ == '__main__':
    from minitest import *

    with test_case("last_function"):
        with test("test"):
            atexit.register(last_two)
            raise "some error"
            # test_some()
            # test_some()
            pass