from cStringIO import StringIO
import sys

class capture_output(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self
    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        sys.stdout = self._stdout

def print_msg(msg):
    print msg
    return msg


if __name__ == '__main__':
    from minitest import *

    with test(capture_output):
        with capture_output() as output:
            result = print_msg("mm")
            # raise Exception("ll")
        output.must_equal(['mm'])
        result.must_equal("mm")

