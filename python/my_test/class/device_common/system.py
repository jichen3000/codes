class System:
    def some(self):
        return self.__class__.__module__+"."+self.__class__.__name__
    def common(self):
        return "common"

if __name__ == '__main__':
    from minitest import *

    with test(System):
        System().some().p()