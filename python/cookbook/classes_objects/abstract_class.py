from abc import ABCMeta, abstractmethod
class IStream(object): 
    __metaclass__ = ABCMeta
    @abstractmethod
    def read(self, maxbytes=-1): 
        pass
    @abstractmethod
    def write(self, data): 
        pass

class SocketStream(IStream):
    def read(self, maxbytes=-1):
        pass
    def write(self, data):
        pass

def serialize(obj, stream):
    if not isinstance(stream, IStream):
        raise TypeError('Expected an IStream')
    return True

if __name__ == '__main__':
    from minitest import *

    with test(IStream):
        (lambda : IStream()).must_raise(TypeError, 
                "Can't instantiate abstract class IStream with abstract methods read, write")
        serialize(None, SocketStream()).must_true()

    with test("register"):
        import io
        # Register the built-in I/O classes as supporting our interface
        IStream.register(io.IOBase)
        isinstance(io.IOBase(), IStream).must_true()

