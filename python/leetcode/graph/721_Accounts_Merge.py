class Solution(object):

    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        parents = {}
        def find(src):
            cur = src
            while cur in parents:
                cur = parents[cur]
            union(src, cur)
            return cur
        def union(src, dst):
            if src != dst:
                parents[src] = dst
        mem = {}
        for i, l in enumerate(accounts):
            name = l[0]
            index = i
            for email in l[1:]:
                if email in mem:
                    p = find(mem[email])
                    ip = find(i)
                    union(p, ip)
                else:
                    mem[email] = i
        res = [None] * len(accounts)
        for i, l in enumerate(accounts):
            name = l[0]
            p = find(i)
            if res[p]:
                res[p][1] |= set(l[1:])
            else:
                res[p] = [name, set(l[1:])]
        # print(res)
        results = []
        for l in res:
            if l:
                l[1] = list(l[1])
                l[1].sort()
                # l.p()
                results += [l[0]] + l[1],
        return results
        
if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        Solution().accountsMerge([
                ["John","johnsmith@mail.com","john_newyork@mail.com"],
                ["John","johnsmith@mail.com","john00@mail.com"],
                ["Mary","mary@mail.com"],
                ["John","johnnybravo@mail.com"]]).must_equal([
                ["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],
                ["Mary","mary@mail.com"],
                ["John","johnnybravo@mail.com"]])


