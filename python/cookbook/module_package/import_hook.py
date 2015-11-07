import importlib
import sys
from collections import defaultdict

_post_import_hooks = defaultdict(list)

class PostImportFinder(object): 
    def __init__(self):
        self._skip = set()
    def find_module(self, fullname, path=None): 
        print "find_module:", fullname
        if fullname in self._skip:
            return None 
        self._skip.add(fullname) 
        return PostImportLoader(self)

class PostImportLoader(object):
    def __init__(self, finder):
        self._finder = finder
    def load_module(self, fullname): 
        print "load_module:", fullname
        # print fullname
        importlib.import_module(fullname)
        module = sys.modules[fullname]
        for func in _post_import_hooks[fullname]:
            func(module) 
        self._finder._skip.remove(fullname) 
        return module

def when_imported(fullname): 
    def decorate(func):
        if fullname in sys.modules: 
            func(sys.modules[fullname])
        else: 
            _post_import_hooks[fullname].append(func)
        return func 
    return decorate

sys.meta_path.insert(0, PostImportFinder())

@when_imported('threading')
def warn_threads(mod):
    print('Threads? Are you crazy?')
import threading
# cannot import minitest, this maybe too complex
# import minitest
# if __name__ == '__main__':
#     from minitest import *

#     with test():
#         with capture_output as output:
#             import threading
#         output.must_equal([''])