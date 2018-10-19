import sys
from collections import Counter
from math import factorial
    
def handle_two(s1, s2):
    # (s1,s2).p()
    return Counter(s1) == Counter(s2)

def cnr(n,k):
    return factorial(n)/(factorial(n-k)*factorial(k))

def get_all_indexs(the_list, item):
    return [i for i,v in enumerate(the_list) if v==item]

# this work in time
def handle3(s):
    s_len = len(s)
    if s_len <= 1:
        return 0
    if s_len == 2:
        if s[0] == s[1]:
            return 1
        else:
            return 0
    if s_len > 2:
        right_s = s[1:]
        pre_result = handle3(right_s)
        if all(s[0]==v for v in right_s):
            return pre_result + cnr(s_len, 2)
        sum_v = pre_result
        if pre_result > 0 or right_s.count(s[0]) > 0:
            for k in range(1,s_len):
                # k.p()
                for i in range(1,len(right_s)-k+2):
                    if s[0:k].count(s[0]) == s[i:i+k].count(s[0]):
                        sum_v += handle_two(s[0:k],s[i:i+k])
                # sum_v += sum([handle_two(s[0:k],s[i:i+k]) for i in range(1,len(right_s)-k+2)])
                # sum_v.p()
        return sum_v

def handle2(s):
    s_len = len(s)
    if s_len <= 1:
        return 0
    if s_len == 2:
        if s[0] == s[1]:
            return 1
        else:
            return 0
    if s_len > 2:
        right_s = s[1:]
        pre_result = handle2(right_s)
        if all(s[0]==v for v in right_s):
            return pre_result + cnr(s_len, 2)
        sum_v = pre_result
        # pre_result.p()
        # right_s.count(s[0]).
        # in_count = right_s.count(s[0])
        all_indexs = filter(lambda i: i>0, get_all_indexs(s, s[0]))
        # s.p()
        # all_indexs.p()
        if len(all_indexs) > 0:
            for j in all_indexs:
                # j.p()
                # for this two single char
                syn_count = 1
                # left side
                # for k in range(1,j):
                #     [[0,k+1],[j-k,j+1]].p()
                #     (s[0:k+1],s[j-k:j+1]).p()
                syn_count += sum([handle_two(s[0:k+1],s[j-k:j+1]) for k in range(1,j)])
                # syn_count.p()
                # right side
                for k in range(1,s_len - j):
                    # [(0,k+1),(j,j+k+1)].p()
                    # (s[0:k+1],s[j:j+k+1]).p()
                    if s[j+k] != s[0]:
                        syn_count += handle_two(s[0:k+1],s[j:j+k+1])
                    # else:
                    #     print("pss")
                # syn_count.p()
                sum_v += syn_count 

        return sum_v

def handle_long_time(s):
    s_len = len(s)
    if s_len <= 1:
        return 0
    if s_len == 2:
        if s[0] == s[1]:
            return 1
        else:
            return 0
    if s_len > 2:
        right_s = s[1:]
        pre_result = handle_long_time(right_s)
        sum_v = pre_result
        if pre_result > 0 or right_s.count(s[0]) > 0:
            for k in range(1,s_len):
                # k.p()
                sum_v += sum([handle_two(s[0:k],s[i:i+k]) for i in range(1,len(right_s)-k+2)])
                # sum_v.p()
        return sum_v

def handle(s):
    s_len = len(s)
    if s_len <= 1:
        return 0
    if s_len == 2:
        if s[0] == s[1]:
            return 1
        else:
            return 0
    if s_len > 2:
        right_s = s[1:]
        pre_result = handle(right_s)
        if all(s[0]==v for v in right_s):
            return pre_result + cnr(s_len, 2)
        s0_count = right_s.count(s[0])
        # s0_count.p()
        # pre_result.p()
        if s0_count>0:
            if pre_result > 0:
                # len(right_s).p()
                # all_indexs = filter(lambda i: i>1, get_all_indexs(s, s[0]))
                # inside_count = 0
                # all_indexs.p()
                # for j in all_indexs:
                #     for k in range(2,j-1):
                #         inside_count += sum([handle_two(s[0:k],s[i:i+k]) for i in range(1,len(right_s)-k+2)])
                # pre_result += inside_count 
                # inside_count.p()

                all_indexs = filter(lambda i: i>1, get_all_indexs(right_s, s[0]))
                # all_indexs.p()
                for j in all_indexs:
                    syn_count = 0
                    for i in range(0,j/2+j%2):
                        # i.p()
                        if right_s[i] == right_s[j-1-i]:
                            syn_count += 1
                    if syn_count > 0:
                        pre_result += syn_count + syn_count - 1 - j%2
            if s[0] == right_s[0]:
                return pre_result + s0_count*2 - 1
            else:
                return pre_result + s0_count*2 
        else:
            return pre_result


# q = int(raw_input().strip())
# for a0 in xrange(q):
#     s = raw_input().strip()
#     result = handle(s)
#     print(result)

from multiprocessing.pool import ThreadPool, Pool
if __name__ == '__main__':
    from minitest import *


    # with test("thread"):
        # pool = Pool(processes=2)
        # # pool = Pool(processes=2)
        # # result = pool.apply_async(handle,("aa",))
        # test_a = "ifailuhkqqhucpoltgtyovarjsnrbfpvmupwjjjfiwwhrlkpekxxnebfrwibylcvkfealgonjkzwlyfhhkefuvgndgdnbelgruel"
        # test_b = "dbcfibibcheigfccacfegicigcefieeeeegcghggdheichgafhdigffgifidfbeaccadabecbdcgieaffbigffcecahafcafhcdg"
        # # handle_long_time(test_a)
        # # handle_long_time(test_b).must_equal(1464)
        # # result = pool.map(handle_long_time,(test_a,test_b))
        # # result.p()
        # result1 = pool.apply_async(handle_long_time,(test_a,))
        # result2 = pool.apply_async(handle_long_time,(test_b,))
        # print("waiting get")
        # result1.get().p()
        # result2.get().p()
#         handle("ifailuhkqqhucpoltgtyovarjsnrbfpvmupwjjjfiwwhrlkpekxxnebfrwibylcvkfealgonjkzwlyfhhkefuvgndgdnbelgruel").must_equal(399)
#         # handle("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").must_equal(166650)

    with test(handle):
        # handle("aa").must_equal(1)
        # handle("aaa").must_equal(4)
        # handle("abba").must_equal(4)
        # handle_long_time("aa").must_equal(1)
        # handle_long_time("aaa").must_equal(4)
        # handle_long_time("aaaa").must_equal(10)
        # handle_long_time("aba").must_equal(2)
        # handle2("aaaa").must_equal(10)
        # handle_long_time("aaaa").must_equal(10)
        # handle2("aaaaa").must_equal(20)
        # handle_long_time("aaaaa").must_equal(20)

        # handle2("bcecba").must_equal(6)
        # handle_long_time("bcecba").must_equal(6)
        # handle2("abcecba").must_equal(12)
        # handle_long_time("abcecba").must_equal(12)
        # handle2("bccba").must_equal(4)
        # handle_long_time("bccba").must_equal(4)
        # handle2("abccba").must_equal(9)
        # handle_long_time("abccba").must_equal(9)
        # handle2("abcba").must_equal(6)
        # handle_long_time("abcba").must_equal(6)
        # handle2("aabcba").must_equal(9)
        # handle_long_time("aabcba").must_equal(9)
        # handle2("aabcbaa").must_equal(18)
        # handle_long_time("aabcbaa").must_equal(18)
        # handle2("baabcbaa").must_equal(27)
        # handle_long_time("baabcbaa").must_equal(27)

        # handle2("ifailuhkqqhucpoltgtyovarjsnrbfpvmupwjjjfiwwhrlkpekxxnebfrwibylcvkfealgonjkzwlyfhhkefuvgndgdnbelgruel").must_equal(399)
        # handle3("ifailuhkqqhucpoltgtyovarjsnrbfpvmupwjjjfiwwhrlkpekxxnebfrwibylcvkfealgonjkzwlyfhhkefuvgndgdnbelgruel").must_equal(399)
        # handle_long_time("ifailuhkqqhucpoltgtyovarjsnrbfpvmupwjjjfiwwhrlkpekxxnebfrwibylcvkfealgonjkzwlyfhhkefuvgndgdnbelgruel").must_equal(399)
        # handle2("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").must_equal(166650)
        handle3("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").must_equal(166650)
        # handle_long_time("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").must_equal(166650)
        # handle_long_time("dbcfibibcheigfccacfegicigcefieeeeegcghggdheichgafhdigffgifidfbeaccadabecbdcgieaffbigffcecahafcafhcdg").must_equal(1464)
        # handle2("dbcfibibcheigfccacfegicigcefieeeeegcghggdheichgafhdigffgifidfbeaccadabecbdcgieaffbigffcecahafcafhcdg").must_equal(1464)
        # handle3("dbcfibibcheigfccacfegicigcefieeeeegcghggdheichgafhdigffgifidfbeaccadabecbdcgieaffbigffcecahafcafhcdg").must_equal(1464)



