## matrix and using multiple options
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        print word1,word2
        n1 = len(word1)
        n2 = len(word2)
        # if n2 == 0:
        #     return 0
        if n1 == 0:
            return n2
        if n2 == 0:
            return n1
        if word1[-1] == word2[-1]:
            return self.minDistance(word1[:n1-1],word2[:n2-1])
        else:
            return min(self.minDistance(word1[:n1],word2[:n2-1]), 
                       self.minDistance(word1[:n1-1],word2[:n2-1]),
                       self.minDistance(word1[:n1-1],word2[:n2])) + 1

#             if n1 == n2:
#             elif n1 > n2:
#                 return self.minDistance(word1[:n1-1],word2[:n2]) + 1
#             else:
#                 return self.minDistance(word1[:n1],word2[:n2-1]) + 1

    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        n1 = len(word1)
        n2 = len(word2)
        dp = [[0] * (n2+1) for _ in range(n1+1)]
        for i in range(n1+1):
            for j in range(n2+1):
                if i == 0 or j == 0:
                    dp[i][j] = max(i,j)
                else:
                    if word1[i-1] == word2[j-1]:
                        dp[i][j] = dp[i-1][j-1]
                    else:
                        dp[i][j] = min(dp[i-1][j],
                                dp[i][j-1],
                                dp[i-1][j-1]) + 1
        return dp[-1][-1]

# str1 = "sunday"
# str2 = "saturday"