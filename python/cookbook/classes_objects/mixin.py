from collections import defaultdict

class LoggedMappingMixin(object): 
    '''
    Add logging to get/set/delete operations for debugging. 
    '''
    __slots__ = ()
    def __getitem__(self, key): 
        print('Getting ' + str(key)) 
        return super(LoggedMappingMixin, self).__getitem__(key)
    def __setitem__(self, key, value):
        print('Setting {} = {!r}'.format(key, value)) 
        return super(LoggedMappingMixin, self).__setitem__(key, value)
    def __delitem__(self, key): 
        print('Deleting ' + str(key)) 
        return super(LoggedMappingMixin, self).__delitem__(key)

class MyDict(LoggedMappingMixin, dict):
    pass

if __name__ == '__main__':
    from minitest import *

    with test(MyDict):
        my = MyDict()
        my['x'] = 23
        pass