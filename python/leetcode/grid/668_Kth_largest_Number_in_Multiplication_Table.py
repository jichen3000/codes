import heapq
class Solution(object):
    def findKthNumber_timelimited(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        directions = [(1,0),(0,1)]
        # visited = [[False for j in xrange(n)] for i in xrange(m)]
        def get_adjs(i,j):
            return [((i+x+1)*(j+y+1),i+x,j+y) for x,y in directions 
                    if i+x>=0 and i+x<m and j+y>=0 and j+y<n]
        if k > m * n or k <=0:
            return None
        if k == 1:
            return 1
        acc = [(1,0,0)]
        # visited[0][0] = True
        while k>0:
            v, i, j = heapq.heappop(acc)
            # (v, i, j).p()
            if k == 1:
                len(acc).p()
                return  v
            for cur in get_adjs(i,j):
                # cur.p()
                # visited[cur[1]][cur[2]] = True
                if cur not in acc:
                    heapq.heappush(acc, cur)
            k -= 1
    def findKthNumber_timelimited2(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        directions = [(1,0),(0,1)]
        # visited = [[False for j in xrange(n)] for i in xrange(m)]
        def get_adjs(i,j):
            # if i < j and j+1 < n:
            #     return [((i+1)*(j+2),i, j+1)]
            # if i > j and i+1 < m:
            #     return [((i+2)*(j+1),i+1, j)]
            # if i == j and i+1 < m and j+1 < n:
            #     return [((i+2)*(j+2),i+1, j+1)]
            # for x,y in directions:
            r = [((i+x+1)*(j+y+1),i+x,j+y) for x,y in directions if i+x<m and j+y<n]
            # if len(r) == 1:
            #     return r
            if len(r) == 2:
                if r[0][0] < r[1][0]:
                    return [r[0]]
                elif r[0][0] > r[1][0]:
                    return [r[1]]
            return r
        if k > m * n or k <=0:
            return None
        if k == 1:
            return 1
        acc = [(1,0,0)]
        if n > 1:
            heapq.heappush(acc, (2,0,1))
        if m > 1:
            heapq.heappush(acc, (2,1,0))
        if n > 1 and m > 1:
            heapq.heappush(acc, (4,1,1))
        # visited[0][0] = True
        while k>0:
            # acc.p()
            v, i, j = heapq.heappop(acc)
            # (v, i, j,k).p()
            if k == 1:
                len(acc).p()
                return  v
            adjs = get_adjs(i,j)
            if i == j and i+1<m and j+1<n:
                adjs += ((i+2)*(j+2), i+1, j+1),
            for cur in adjs:
                # cur.p()
                # visited[cur[1]][cur[2]] = True
                if cur not in acc:
                    # cur.p()
                    heapq.heappush(acc, cur)

            # adjs = get_adjs(i,j)
            # if len(adjs) > 0:
            #     cur = min(adjs)
            #     if cur not in acc:
            #         cur.p()
            #         heapq.heappush(acc, cur)
            k -= 1
          
    def findKthNumber(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        directions = [(1,0),(0,1),(1,1)]
        # visited = [[False for j in xrange(n)] for i in xrange(m)]
        def get_adjs(i,j):
            if i < j and j+1 < n:
                return [((i+1)*(j+2),i, j+1)]
            if i > j and i+1 < m:
                return [((i+2)*(j+1),i+1, j)]
            # if i == j:
            # #     return [((i+2)*(j+2),i+1, j+1)]
            # # for x,y in directions:
            #     return [((i+x+1)*(j+y+1),i+x,j+y) for x,y in directions if i+x<m and j+y<n]
            return []
        if k > m * n or k <=0:
            return None
        if k == 1:
            return 1
        acc = [(1,0,0)]
        # if n > 1:
        #     heapq.heappush(acc, (2,0,1))
        # if m > 1:
        #     heapq.heappush(acc, (2,1,0))
        # if n > 1 and m > 1:
        #     heapq.heappush(acc, (4,1,1))

        # visited[0][0] = True
        square_i = 0
        while k>0:
            # acc.p()
            v, i, j = heapq.heappop(acc)
            # (v, i, j,k).p()
            if k == 1:
                len(acc).p()
                return  v
            if v == (square_i + 1) ** 2:
                adjs = [((square_i+x+1)*(square_i+y+1),square_i+x,square_i+y) for x,y in directions if square_i+x<m and square_i+y<n] + get_adjs(i,j)
                square_i += 1
            else:
                adjs = get_adjs(i,j)
            # (i,j,adjs).p()
            # if i == j and i+1<m and j+1<n:
            #     adjs += ((i+2)*(j+2), i+1, j+1),
            for cur in adjs:
                # cur.p()
                # visited[cur[1]][cur[2]] = True
                # if cur not in acc:
                    # cur.p()
                heapq.heappush(acc, cur)

            # adjs = get_adjs(i,j)
            # if len(adjs) > 0:
            #     cur = min(adjs)
            #     if cur not in acc:
            #         cur.p()
            #         heapq.heappush(acc, cur)
            k -= 1
          
if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        # Solution().findKthNumber(3,3,5).must_equal(3)
        # Solution().findKthNumber(2,3,6).must_equal(6)
        # Solution().findKthNumber(10,10,99).must_equal(1470)
        # Solution().findKthNumber(1000,1000,9999).must_equal(1470)
        # Solution().findKthNumber(10000,10000,99999).must_equal(10755)
        Solution().findKthNumber(10000,10000,999999).must_equal(10755)
        # Solution().findKthNumber(9895,28405,100787757).must_equal(6)
   