#!/bin/python

import sys

def saveThePrisoner(n, m, s):
    # Complete this function
    result =  (m+s-1) % n
    if result == 0:
        return n
    return result

print(355311663 % 158)
print(saveThePrisoner(158,355311663,2))
# t = int(raw_input().strip())
# for a0 in xrange(t):
#     n, m, s = raw_input().strip().split(' ')
#     n, m, s = [int(n), int(m), int(s)]
#     result = saveThePrisoner(n, m, s)
#     print(result)