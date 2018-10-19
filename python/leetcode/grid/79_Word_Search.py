class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m = len(board)
        if m == 0: return False
        n = len(board[0])
        wn = len(word)
        visited = [ [False] * n for _ in range(m)]
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        def get_adjs(i, j, wi):
            res = []
            for di, dj in dirs:
                ni, nj = di + i, dj + j
                if ni >= 0 and ni < m and nj>=0 and nj < n \
                        and not visited[ni][nj] and word[wi] == board[ni][nj]:
                    res += (ni,nj),
            return res
        def dfs(i, j, wi):
            if wi == wn - 1: return True
            adjs = get_adjs(i, j, wi+1)
            for ni, nj in adjs:
                visited[ni][nj] = True
                if dfs(ni,nj,wi+1):
                    return True
                visited[ni][nj] = False
            return False
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    visited[i][j] = True
                    if dfs(i,j,0):
                        return True
                    visited[i][j] = False
        return False
                    
        
        