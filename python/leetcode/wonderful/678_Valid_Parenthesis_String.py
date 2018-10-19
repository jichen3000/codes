class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0:
            return True
        cache= {}
        cache["("] = 0
        cache["*)"] = 0
        cache["*("] = 0
        for cur_s in s:
            if cur_s == "(":
                cache["*)"] = min(cache["("],cache["*)"])
                cache["("] += 1
            elif cur_s == "*":
                cache["*("] += 1
                cache["*)"] += 1
            elif cur_s == ")":
                if cache["("] > 0:
                    cache["("] -= 1
                elif cache["*("] > 0:
                    cache["*("] -= 1
                    if cache["*)"] > 0:
                        cache["*)"] -= 1
                else:
                    return False
        # cache.p()
        return cache["*)"] >= cache["("]
            
if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        Solution().checkValidString("*())").must_equal(True)
        Solution().checkValidString("(*)").must_equal(True)
        Solution().checkValidString("(*))").must_equal(True)
        Solution().checkValidString("(*)))").must_equal(False)
        Solution().checkValidString("(*()").must_equal(True)
        Solution().checkValidString("(**((*").must_equal(False)



        # Solution().combinationSum([1,2],4).must_equal([[1, 1, 1, 1], [2, 2], [1, 1, 2]])
        # Solution().subsetsWithDup([4,4,4,1,4]).p()