# https://docs.python.org/3/library/contextlib.html
from contextlib import contextmanager
from urllib.request import urlopen

@contextmanager
def tag(name):
    print("<%s>" % name)
    yield
    print("</%s>" % name)

with tag("h1"):
    print ("foo")

@contextmanager
def closing(thing):
    try:
        yield thing
    finally:
        thing.close()

with closing(urlopen('http://www.python.org')) as page:
    for line in page:
        print(line)  