import json
import pkgutil

if __name__ == '__main__':
    from minitest import *

    with test(pkgutil):
        __package__.pp()
        data= pkgutil.get_data(__name__, 'test.json')
        json.loads(data).pp()