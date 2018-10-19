# Python program to implement Manacher's Algorithm
  
# def findLongestPalindromicString(text):
def find_lps(text):
    origin_n = len(text)
    if origin_n == 0:
        return
    extend_len = 2*origin_n+1    # Position count
    lps_l = [0] * extend_len
    lps_l[1] = 1
    center_i = 1     # centerPosition
    right_border = 2     # centerRightPosition
    right_i = 0    # currentRightPosition
    left_i = 0     # currentLeftPosition
    max_lps_len = 1
    max_lps_center_i = 1
    right_border_diff = -1
  
    for right_i in xrange(2,extend_len):
      
        # get currentLeftPosition left_i for currentRightPosition i
        # since center_i - left_i = right_i - center_i
        left_i = 2*center_i - right_i

        right_border_diff = right_border - right_i
        # (right_i, left_i, center_i, right_border, right_border_diff).p()
        # If currentRightPosition i is within centerRightPosition right_border
        # this is the key, using symmetric to save time
        if right_border_diff > 0:
            lps_l[right_i] = min(lps_l[left_i], right_border_diff)
  
        # Attempt to expand palindrome centered at currentRightPosition i
        # Here for odd positions, we compare characters and
        # if match then increment LPS Length by ONE
        # If even position, we just increment LPS by ONE without any character comparison
        # since in even position is |
        while right_i+lps_l[right_i] < extend_len and right_i > lps_l[right_i] and \
                ( (right_i+lps_l[right_i]+1) % 2 == 0 or \
                ( (right_i+lps_l[right_i]+1)/2 < origin_n and \
                text[(right_i+lps_l[right_i]+1)/2] == text[(right_i-lps_l[right_i]-1)/2])):
            lps_l[right_i]+=1
  
        # Track max_lps_len
        if lps_l[right_i] > max_lps_len:        
            max_lps_len = lps_l[right_i]
            max_lps_center_i = right_i
  
        # If palindrome centered at currentRightPosition i
        # expand beyond centerRightPosition right_border,
        # adjust centerPosition center_i based on expanded palindrome.
        if right_i + lps_l[right_i] > right_border:
            center_i = right_i
            right_border = right_i + lps_l[right_i]
        # lps_l[right_i].p()
  
    # Uncomment it to print LPS Length array
    # printf("%d ", lps_l[right_i]);
    p_start = (max_lps_center_i - max_lps_len) / 2
    p_end = p_start + max_lps_len - 1
    return text[p_start:p_end+1]

if __name__ == '__main__':
    from minitest import *

    with test(find_lps):
        find_lps("b").must_equal("b")
        find_lps("babcbabcbaccba").must_equal("abcbabcba")
        # find_lps("abaaba").must_equal("abaaba")
        # find_lps("abababa").must_equal("abababa")
        # find_lps("abcbabcbabcba").must_equal("abcbabcbabcba")
        # find_lps("forgeeksskeegfor").must_equal("geeksskeeg")
        # find_lps("caba").must_equal("aba")
        # find_lps("abacdfgdcaba").must_equal("aba")
        # find_lps("abacdfgdcabba").must_equal("abba")
        # find_lps("abacdedcaba").must_equal("abacdedcaba")
