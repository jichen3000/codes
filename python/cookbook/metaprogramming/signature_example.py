from funcsigs import signature

def spam(x,y,z=42):
    return (x,y,z)

if __name__ == '__main__':
    from minitest import *

    with test(signature):
        sig = signature(spam)
        sig.__str__().must_equal('(x, y, z=42)')
        sig.parameters['y'].name.must_equal('y')
        # print dir(sig.parameters['y'].default)
            # print "mm"
        # sig.parameters['y'].default.__str__().must_equal(42)
        sig.parameters['y'].kind.__str__().must_equal(
                'POSITIONAL_OR_KEYWORD')

        sig.parameters['z'].name.must_equal('z')
        sig.parameters['z'].default.must_equal(42)
        sig.parameters['z'].kind.__str__().must_equal(
                'POSITIONAL_OR_KEYWORD')

        bound_types = sig.bind_partial(int,z=int)
        bound_types.arguments.__str__().must_equal(
            "OrderedDict([('x', <type 'int'>), ('z', <type 'int'>)])")