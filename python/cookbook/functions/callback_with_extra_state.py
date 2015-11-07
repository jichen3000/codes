def apply_async(func, args, callback):
    result = func(*args)

    return callback(result)

def return_result_msg(result):
    msg =  "Got {}".format(result)
    # print msg
    return msg

def add(x, y):
    return x+y

class ResultHandler(object):
    def __init__(self):
        self.sequence = 0

    def handler(self, result):
        self.sequence += 1
        return "[{}] Got {}".format(self.sequence, result)

def make_handler_closure_hash():
    inner_dict ={'sequence':0}
    # sequence = 0
    def handler(result):
        # in python2 there is no nonlocal, so using dict
        # nonlocal sequence
        # sequence += 1
        inner_dict['sequence'] += 1
        # return "[{}] Got {}".format(sequence, result)
        return "[{}] Got {}".format(inner_dict['sequence'], result)
        # return "Got {}".format(result)
    return handler

def make_handler_closure_attribute():
    def handler(result):
        handler.sequence += 1
        return "[{}] Got {}".format(handler.sequence, result)
    handler.sequence = 0
    return handler

def make_handler_coroutine(): 
    sequence = 0
    result = 0
    while True:
        # firstly get the result from "[{}] Got {}".format(sequence, result)
        # and return that result
        # next time, 'result' will get the value from send.
        result = yield "[{}] Got {}".format(sequence, result)
        sequence += 1
        # return "[{}] Got {}".format(sequence, result)
        # print('[{}] Got: {}'.format(sequence, result))

class Sequence:
    def __init__(self):
        self.sequence = 0

def handler_with_seq(result, seq):
    seq.sequence += 1
    return "[{}] Got {}".format(seq.sequence, result)

if __name__ == '__main__':
    from minitest import *

    with test("without extra state"):
        apply_async(add, (2, 3), 
                callback=return_result_msg).must_equal("Got 5")
        apply_async(add, ("hello","world"), 
                callback=return_result_msg).must_equal("Got helloworld")
    
    with test("using class"):
        result_handler = ResultHandler()
        apply_async(add, (2, 3), 
                callback=result_handler.handler).must_equal("[1] Got 5")
        apply_async(add, ("hello","world"), 
                callback=result_handler.handler).must_equal("[2] Got helloworld")

    with test("using closure hash"):
        handler = make_handler_closure_hash()
        apply_async(add, (2, 3), 
                callback=handler).must_equal("[1] Got 5")
        apply_async(add, ("hello","world"), 
                callback=handler).must_equal("[2] Got helloworld")

    with test("using closure attribute"):
        handler = make_handler_closure_attribute()
        apply_async(add, (2, 3), 
                callback=handler).must_equal("[1] Got 5")
        apply_async(add, ("hello","world"), 
                callback=handler).must_equal("[2] Got helloworld")

    with test("coroutine, it's the best pratice."):
        handler = make_handler_coroutine()
        next(handler)
        apply_async(add, (2, 3), 
                callback=handler.send).must_equal("[1] Got 5")
        apply_async(add, ("hello","world"), 
                callback=handler.send).must_equal("[2] Got helloworld")

    with test("using sequence class"):
        from functools import partial
        seq = Sequence()
        apply_async(add, (2, 3), 
                callback=partial(handler_with_seq, seq=seq)).must_equal("[1] Got 5")
        apply_async(add, ("hello","world"), 
                callback=partial(handler_with_seq, seq=seq)).must_equal("[2] Got helloworld")

