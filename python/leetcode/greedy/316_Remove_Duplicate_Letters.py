from collections import defaultdict, Counter
class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        if n <= 1: return s
        counter = Counter(s)
        visited = defaultdict(lambda: False)
        result = ""
        for c in s:
            counter[c] -= 1
            if visited[c]: continue
            while len(result) > 0 and counter[result[-1]] > 0 and result[-1] > c:
                visited[result[-1]] = False
                result = result[:-1]
            visited[c] = True
            result += c
        return result

    # The basic idea is to find out the smallest result letter by letter (one letter at a time). Here is the thinking process for input "cbacdcbc":

    # find out the last appeared position for each letter;
    # c - 7
    # b - 6
    # a - 2
    # d - 4
    # find out the smallest index from the map in step 1 (a - 2);
    # the first letter in the final result must be the smallest letter from index 0 to index 2;
    # repeat step 2 to 3 to find out remaining letters.
    # the smallest letter from index 0 to index 2: a
    # the smallest letter from index 3 to index 4: c
    # the smallest letter from index 4 to index 4: d
    # the smallest letter from index 5 to index 6: b
    # so the result is "acdb"

    # Notes:

    # after one letter is determined in step 3, it need to be removed from the "last appeared position map", and the same letter should be ignored in the following steps
    # in step 3, the beginning index of the search range should be the index of previous determined letter plus one        
    def removeDuplicateLetters(self, s):
        result = ''
        while s:
            i = min(map(s.rindex, set(s)))
            c = min(s[:i+1])
            result += c
            s = s[s.index(c):].replace(c, '')
        return result

if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        Solution().removeDuplicateLetters("bcabc").must_equal("abc")
        Solution().removeDuplicateLetters("bceabc").must_equal("bcea")
        Solution().removeDuplicateLetters("ebceabc").must_equal("bcea")
        Solution().removeDuplicateLetters("cbacdcbc").must_equal("acdb")
        Solution().removeDuplicateLetters("ccacbaba").must_equal("acb")
        Solution().removeDuplicateLetters("abacb").must_equal("abc")
        Solution().removeDuplicateLetters("abacbijhij").must_equal("abchij")