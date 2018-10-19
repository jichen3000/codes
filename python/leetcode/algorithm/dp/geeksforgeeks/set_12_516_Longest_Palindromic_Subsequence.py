class Solution(object):

    def longestPalindromeSubseq(self, the_s):
        '''
        since it only depends on dp[i+1][j-1], and dp[i][j-1], dp[i+1][j],
        it could be only use array
        '''
        n = len(the_s)
        dp = [[1 for _ in xrange(n)] for _ in xrange(n)]
        for i in xrange(n-1):
            if the_s[i] == the_s[i+1]:
                dp[i][i+1] = 2
        for l in xrange(2,n):
            for i in xrange(n-l):
                j = i + l
                # print(i,j)
                if the_s[i] == the_s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i+1][j])
        # print dp
        return dp[0][n-1]

    def longestPalindromeSubseq(self, the_s):
        n = len(the_s)
        dp = [1 for _ in xrange(n)]
        # pre = 1
        pre = dp
        pre_pre = dp
        for l in xrange(1,n):
            pre = dp[:]
            for i in xrange(n-l):
                j = i + l
                if the_s[i] == the_s[j]:
                    dp[i] = pre_pre[i+1] + 2
                else:
                    dp[i] = max(dp[i], dp[i+1])
            pre_pre = pre[:]
            pre = dp[:]
            # (l,dp).p()
        # print dp
        return dp[0]
        # 

if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        # a = "aabaaba"
        # Solution().longestPalindromeSubseq(a).must_equal(6)
        a = "euazbipzncptldueeuechubrcourfpftcebikrxhybkymimgvldiwqvkszfycvqyvtiwfckexmowcxztkfyzqovbtmzpxojfofbvwnncajvrvdbvjhcrameamcfmcoxryjukhpljwszknhiypvyskmsujkuggpztltpgoczafmfelahqwjbhxtjmebnymdyxoeodqmvkxittxjnlltmoobsgzdfhismogqfpfhvqnxeuosjqqalvwhsidgiavcatjjgeztrjuoixxxoznklcxolgpuktirmduxdywwlbikaqkqajzbsjvdgjcnbtfksqhquiwnwflkldgdrqrnwmshdpykicozfowmumzeuznolmgjlltypyufpzjpuvucmesnnrwppheizkapovoloneaxpfinaontwtdqsdvzmqlgkdxlbeguackbdkftzbnynmcejtwudocemcfnuzbttcoew"
        Solution().longestPalindromeSubseq(a).must_equal(159)



