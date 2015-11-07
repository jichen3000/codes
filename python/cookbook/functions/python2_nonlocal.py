def outer():
    def inner():
        inner.y += 1
        return inner.y
    inner.y = 0
    return inner

f = outer()
g = outer()
# print(f(), f(), g(), f(), g()) #prints (1, 2, 1, 3, 2)

if __name__ == '__main__':
    from minitest import *

    with test(outer):
        [f(), f(), g(), f(), g()].must_equal([1, 2, 1, 3, 2])
        pass