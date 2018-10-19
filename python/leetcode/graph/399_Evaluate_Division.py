class Solution:
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        parents = {}
        mem = set()
        def find(src):
            origin, v =src, 1.0
            while src in parents:
                src, cur_v = parents[src]
                v *= cur_v
            if src != origin:
                parents[origin] = (src, v)
            return src, v
        def union(src, dst, v):
            src_parent, src_v = find(src)
            dst_parent, dst_v = find(dst)
            parents[src_parent] = (dst_parent, v * dst_v / src_v )
            mem.add(src)
            mem.add(dst)
        res = []
        for (src, dst), v in zip(equations, values):
            union(src, dst, v)
        # print(mem)
        for src, dst, in queries:
            src_parent, src_v = find(src)
            dst_parent, dst_v = find(dst)
            # print(src, src_parent, src_v)
            # print(dst, dst_parent, dst_v)
            if src in mem and dst in mem and src_parent == dst_parent:
                res += src_v / dst_v,
            else:
                res += -1.0,
        return res

if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        Solution().calcEquation([["x1","x2"],["x2","x3"],["x1","x4"],["x2","x5"]],
                [3.0,0.5,3.4,5.6],
                [["x2","x4"],["x1","x5"],["x1","x3"],["x5","x5"],["x5","x1"],["x3","x4"],["x4","x3"],["x6","x6"],["x0","x0"]]).must_equal(
                [1.1333333333333333,16.8,1.5,1.0,0.05952380952380952,2.2666666666666666,0.4411764705882353,-1.0,-1.0])
