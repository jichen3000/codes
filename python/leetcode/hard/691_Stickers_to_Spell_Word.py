from collections import Counter
class Solution(object):
    # 30mins get this solution
    def minStickers_timelimited(self, stickers, target):
        """
        :type stickers: List[str]
        :type target: str
        :rtype: int
        """
        tc = Counter(target)
        sc_list = [Counter(s) for s in stickers]
        # count = [0]
        def get_common(c1, c2):
            larger = c1 - c2
            if larger == c1: 
                return None
            else:
                return c1 - larger
        def inner(sc_list, tc):
            # count[0] += 1
            # if count[0] > 60: exit()
            # sc_list.p()
            # tc.p()
            if len(tc) == 0: return 0
            if len(sc_list) == 0: return 999999
            results = []
            for i in range(len(sc_list)):
                sc = sc_list[i]
                common = get_common(sc, tc)
                if common:
                    results += inner(sc_list, tc-common) + 1,
                else: 
                    results += inner(sc_list[:i]+sc_list[i+1:], tc),
            if len(results) == 0: return False
            return min(results)
        return inner(sc_list, tc)
        
                    
        
        
if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        Solution().minStickers(["with","example","science"], "thehat").p()