# https://leetcode.com/problems/shortest-palindrome/
# Given a string S, you are allowed to convert it to a palindrome by adding characters in front of it. 
# Find and return the shortest palindrome you can find by performing this transformation.

# For example:
# Given "aacecaaa", return "aaacecaaa".
# Given "abcd", return "dcbabcd".


## big o is 3n**2
def in_list(the_list, index):
    return index >= 0 and index < len(the_list)

def get_near_palindrome_pairs(the_str):
    result = []
    for i in range(len(the_str)-1):
        if in_list(the_str, i+2) and the_str[i] == the_str[i+2]:
            result.append((i, i+2))
        if in_list(the_str, i+1) and the_str[i] == the_str[i+1]:
            result.append((i, i+1))
    return result

def get_extend_palindrome(the_str, start_index_pair):
    left_start, right_start = start_index_pair
    i = 0
    while   in_list(the_str, left_start-i) and \
            in_list(the_str, right_start+i) and \
            the_str[left_start-i] == the_str[right_start+i]:
        i += 1
    if i > 0: i -= 1
    return (left_start-i, right_start+i)

def filter_edge_pairs(pairs, length):
    return [pair for pair in pairs if pair[0] == 0 or pair[1] == length-1]

def cal_max_length_pair(pairs):
    if len(pairs) == 0:
        return None
    max_edge_extend = (0,0)
    max_len = 1
    for pair in pairs:
        if pair[1] - pair[0] + 1 > max_len:
            max_edge_extend = pair
            max_len = pair[1] - pair[0] + 1
    return max_edge_extend

def assemble_palindrome(the_str, max_edge_extend):
    if max_edge_extend:
        pair_length = max_edge_extend[1] - max_edge_extend[0] + 1
        if max_edge_extend[0] == 0:
            left_str = the_str[pair_length:]
            return left_str[::-1] + the_str
        else:
            left_str = the_str[0:len(the_str)-pair_length]
            return the_str + left_str[::-1]
    else:
        return the_str[::-1][0:len(the_str)-1] + the_str

def cal_shortest_palindrome(the_str):
    pairs = get_near_palindrome_pairs(the_str)
    extends = [get_extend_palindrome(the_str, pair) for pair in pairs]
    edge_extends = filter_edge_pairs(extends, len(the_str))

    max_edge_extend = cal_max_length_pair(edge_extends)        

    return assemble_palindrome(the_str, max_edge_extend)



if __name__ == '__main__':
    from minitest import *

    with test(in_list):
        in_list(range(8), 0).must_true()
        in_list(range(8), 7).must_true()
        in_list(range(8), 9).must_false()
        in_list(range(8), -1).must_false()
        in_list("123", 2).must_true()
        pass

    with test(get_near_palindrome_pairs):
        get_near_palindrome_pairs("aba").must_equal([(0,2)])
        get_near_palindrome_pairs("aa").must_equal([(0,1)])
        get_near_palindrome_pairs("sdfmaagdsds").must_equal(
                [(4,5),(7, 9), (8, 10)])
        get_near_palindrome_pairs("aaa").must_equal([(0, 2), (0, 1), (1, 2)])
        get_near_palindrome_pairs("aacecaaa").must_equal(
                [(0, 1), (2, 4), (5, 7), (5, 6), (6, 7)])

    with test(get_extend_palindrome):
        get_extend_palindrome("aaa", (0, 2)).must_equal((0, 2))
        get_extend_palindrome("aacecaaa", (2,4)).must_equal((0,6))

    with test(filter_edge_pairs):
        filter_edge_pairs([(0, 1), (2, 4), (5, 7), (5, 6), (6, 7)], 8).must_equal(
                [(0, 1), (5, 7), (6, 7)])

    with test(cal_max_length_pair):
        cal_max_length_pair([(0, 1), (5, 7), (6, 7)]).must_equal(
            (5,7))

    with test(assemble_palindrome):
        assemble_palindrome("abcd", None).must_equal("dcbabcd")
        assemble_palindrome("aacecaaa", (0,6)).must_equal("aaacecaaa")
        assemble_palindrome("hijaacecaa", (3,9)).must_equal("hijaacecaajih")

    with test(cal_shortest_palindrome):
        cal_shortest_palindrome("abcd").must_equal("dcbabcd")
        cal_shortest_palindrome("aacecaaa").must_equal("aaacecaaa")
        cal_shortest_palindrome("hijaacecaa").must_equal("hijaacecaajih")
