class A(object):
    pass


def bind_to_object(self, msg):
    return msg

def bind_to_instance(self, msg):
    return msg


if __name__ == '__main__':
    from minitest import *

    with test(bind_to_object):
        A.bind_to_object = bind_to_object
        a = A()
        a.bind_to_object("mm").must_equal("mm")

    with test(bind_to_instance):
        a = A()
        a.bind_to_instance = bind_to_instance
        (lambda : a.bind_to_instance("mm")).must_raise(TypeError, 
                "bind_to_instance() takes exactly 2 arguments (1 given)")

        import types
        a.bind_to_instance = types.MethodType(bind_to_instance, a)
        a.bind_to_instance("mm").must_equal("mm")

