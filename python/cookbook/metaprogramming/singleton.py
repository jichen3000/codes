class Singleton(type):
    def __init__(self, *args, **kwargs):
        self.__instance = None
        super(Singleton, self).__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs): 
        if self.__instance is None:
            self.__instance = super(Singleton, self).__call__(
                    *args, **kwargs)
        return self.__instance 

# Example
class SingletonSpam(object):
    __metaclass__=Singleton
    def __init__(self):
        print('Creating SingletonSpam')

if __name__ == '__main__':
    from minitest import *

    with test(Singleton):
        with capture_output() as output:
            a = SingletonSpam()
            b = SingletonSpam()
        # only create once
        output.must_equal(['Creating SingletonSpam'])

        a.must_equal(b)