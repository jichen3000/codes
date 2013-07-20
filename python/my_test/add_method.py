import types
def patch_method(target, method):
    setattr(target, method.func_name, types.MethodType(method,target))

if __name__ == '__main__':
    from minitest import *

    class A(object):
        pass

    def method(target,x):
        # print "x=",x
        # print "called from", target
        return x

    # can't set attributes of built-in/extension type 'dict'
    def delete(target, key):
        del target[key]
        return target

    with test_case("test it"):
        with test("patch_method"):
            a = A()
            patch_method(a, method)
            a.method(5).must_equal(5)

        with test("test cannot set attributes to built-in type"):
            # patch_method(dict, delete)
