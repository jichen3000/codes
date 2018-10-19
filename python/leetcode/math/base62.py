ALL = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
NUMBER_SYSTEM_V = 62

def encode(int10):
    p, r = divmod(int10,NUMBER_SYSTEM_V)
    res = [ALL[r]]
    while p > 0:
        p, r = divmod(p,NUMBER_SYSTEM_V)
        res += ALL[r],
    return "".join(reversed(res))

def decode(str62):
    j = 1
    res = 0
    for c in reversed(str62):
        i = ALL.index(c)
        res += i * j
        j *= NUMBER_SYSTEM_V
    return res

if __name__ == '__main__':
    from minitest import *

    with test(encode):
        encode(1234).must_equal("t4")

    with test(decode):
        decode("t4").must_equal(1234)
