# difficult, how to handle keys, has_key, these dict functions

class DictClass(object):
    def __init__(self, entries): 
        self.__dict__.update(**entries)

    def __str__(self):
        return self.__dict__.__str__()
    def __repr__(self):
        return self.__dict__.__repr__()

if __name__ == '__main__':
    from minitest import *

    with test(DictClass):
        configs = DictClass({'a':1,'b':True})
        configs.p()
        pass            