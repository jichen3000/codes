import json
import pkgutil

if __name__ == '__main__':
    from minitest import *

    with test(pkgutil):
        data= pkgutil.get_data("mymodule", 'test.json')
        json.loads(data).pp()