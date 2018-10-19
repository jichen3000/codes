class Solution(object):
    def pyramidTransition(self, bottom, allowed):
        """
        :type bottom: str
        :type allowed: List[str]
        :rtype: bool
        """
        from collections import defaultdict
        from itertools import product
        
        if len(bottom) < 2 or not allowed: 
            return False
        allow_dict = defaultdict(list)
        for w in allowed:
            allow_dict[w[:2]] += w[2],
        # print(allow_dict)
        def dfs(s):
            # print("s: ",s)
            if len(s) == 2:
                return (s[0]+s[1]) in allow_dict
            pos_list = []
            pre = s[0]
            for i in range(1, len(s)):
                two = pre+s[i]
                # print(two)
                if two not in allow_dict:
                    return False
                else:
                    pos_list += allow_dict[two],
                pre = s[i]
            nexts = product(*pos_list)
            for ns in nexts:
                if dfs(ns):
                    return True
            return False
        return dfs(bottom)

    def pyramidTransition(self, bottom, allowed):
        """
        :type bottom: str
        :type allowed: List[str]
        :rtype: bool
        """
        from collections import defaultdict
        from itertools import product
        if len(bottom) <= 1: return False
        allow_dict = defaultdict(list)
        for w in allowed:
            allow_dict[(w[0],w[1])] += w[2],
        def dfs(s):
            if len(s) == 2:
                return (s[0],s[1]) in allow_dict
            nexts = []
            for i in range(1,len(s)):
                nl = allow_dict[(s[i-1], s[i])]
                if not nl:
                    return False
                nexts += nl,
            return any(dfs(ns) for ns in product(*nexts))
        return dfs(bottom)         
if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        Solution().pyramidTransition("ABC", ["ABD","BCE","DEF","FFF"]).must_equal(True)