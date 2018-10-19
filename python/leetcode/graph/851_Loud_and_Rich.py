class Solution:
    def loudAndRich(self, richer, quiet):
        """
        :type richer: List[List[int]]
        :type quiet: List[int]
        :rtype: List[int]
        """
        from collections import defaultdict
        if not quiet: return
        n = len(quiet)
        res = [i for i in range(n)]
        rich_poors = defaultdict(list)
        poor_richs = defaultdict(list)
        for rich, poor in richer:
            if quiet[rich] < quiet[res[poor]]:
                res[poor] = rich
                q = [poor]
                while q:
                    cur = q.pop(0)
                    if quiet[rich] < quiet[res[cur]]:
                        res[cur] = rich
                    for p in rich_poors[cur]:
                        q += p,
            q = [rich]
            while q:
                cur = q.pop(0)
                if quiet[cur] < quiet[res[poor]]:
                    res[poor] = cur
                for p in poor_richs[cur]:
                    q += p,
            rich_poors[rich] += poor,
            poor_richs[poor] += rich,
        return res

    def loudAndRich(self, richer, quiet):
        """
        :type richer: List[List[int]]
        :type quiet: List[int]
        :rtype: List[int]
        """
        from collections import defaultdict
        if not quiet: return
        n = len(quiet)
        res = [i for i in range(n)]
        rich_poors = defaultdict(list)
        for rich, poor in richer:
            if quiet[res[rich]] < quiet[res[poor]]:
                res[poor] = res[rich]
                q = [poor]
                while q:
                    cur = q.pop(0)
                    if quiet[res[rich]] < quiet[res[cur]]:
                        res[cur] = res[rich]
                    for p in rich_poors[cur]:
                        q += p,
            rich_poors[rich] += poor,
        return res

if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        Solution().loudAndRich([[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]],
                [3,2,5,4,6,1,7,0]).must_equal([5,5,2,5,4,5,6,7])
        Solution().loudAndRich([[0,1],[1,2]],
                [0,1,2]).must_equal([0,0,0])



