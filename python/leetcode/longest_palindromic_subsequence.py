import itertools
'''
abc
'''
class Solution(object):
    def iterate_all_combinations(self, the_list):
        for cur_len in xrange(len(the_list),1, -1):
            for subset in itertools.combinations(the_list, cur_len):
                yield subset

    def is_full_palindrome(self, the_s):
        s_len = len(the_s)
        if s_len == 1:
            return True
        elif s_len == 2:
            return the_s[0] == the_s[1]
        for i in range(s_len/2-1,-1,-1):
            if the_s[i] != the_s[s_len-1-i]:
                return False
        return True

    def longestPalindromeSubseq_slow_2_power_n(self, the_s):
        max_length = 0
        s_len = len(the_s)
        if s_len == 1:
            return 1
        for subset in self.iterate_all_combinations(the_s):
            if self.is_full_palindrome(subset):
                return len(subset)
        return 1


    def longestPalindromeSubseq_slow_n_power_n(self, the_s):
        """
        :type the_s: str
        :rtype: int
        """        
        max_length = 0
        s_len = len(the_s)
        if s_len == 1:
            return 1
        elif s_len == 2:
            if the_s[0] == the_s[1]:
                return 2
            else:
                return 1
        elif s_len >= 3:
            if self.is_full_palindrome(the_s):
                return s_len
            else:
                for i in xrange(s_len):
                    cur_p_len = self.longestPalindromeSubseq(the_s[0:i]+the_s[i+1:])
                    if cur_p_len == s_len - 1:
                        return cur_p_len
                    max_length = max(max_length, cur_p_len)
        return max_length

if __name__ == '__main__':
    from minitest import *

    with test("longestPalindromeSubseq"):
        # Solution().longestPalindromeSubseq("abcabcabcabc").p()
        Solution().longestPalindromeSubseq("euazbipzncptldueeuechubrcourfpftcebikrxhybkymimgvldiwqvkszfycvqyvtiwfckexmowcxztkfyzqovbtmzpxojfofbvwnncajvrvdbvjhcrameamcfmcoxryjukhpljwszknhiypvyskmsujkuggpztltpgoczafmfelahqwjbhxtjmebnymdyxoeodqmvkxittxjnlltmoobsgzdfhismogqfpfhvqnxeuosjqqalvwhsidgiavcatjjgeztrjuoixxxoznklcxolgpuktirmduxdywwlbikaqkqajzbsjvdgjcnbtfksqhquiwnwflkldgdrqrnwmshdpykicozfowmumzeuznolmgjlltypyufpzjpuvucmesnnrwppheizkapovoloneaxpfinaontwtdqsdvzmqlgkdxlbeguackbdkftzbnynmcejtwudocemcfnuzbttcoew").p()

    # with test(""):
    #     # the_list = range(10,15)
    #     the_s = "abcd"
    #     for subset in Solution().iterate_all_combinations(the_s):
    #         print subset

