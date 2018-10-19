class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        from heapq import heappop, heappush
        n = len(matrix)
        visited = {(0,0)}
        queue = [(matrix[0][0], 0,0)]
        dirs = [(0, 1), (1,0)]
        while k > 1:
            v, i, j = heappop(queue)
            k -= 1
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if ni < n and nj < n and (ni, nj) not in visited:
                    heappush(queue, (matrix[ni][nj], ni, nj))
                    visited.add((ni,nj))
        return heappop(queue)[0]
                            
                
        
        