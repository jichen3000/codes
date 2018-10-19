class Solution:
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        if not rooms or not rooms[0]:
            return
        m, n = len(rooms), len(rooms[0])
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        def get_adjs(x, y, dist):
            res = []
            for di, dj in dirs:
                i, j = di + x, dj + y
                if i >=0 and i < m and j >= 0 and j < n \
                        and rooms[i][j] > dist:
                    res += (i,j),
            return res
        def set_room(x, y):
            dist = 1
            cur_set = get_adjs(x, y, dist)
            while cur_set:
                temp_set = []
                for i, j in cur_set:
                    rooms[i][j] = dist
                    # print(i,j,rooms[i][j])
                    temp_set += get_adjs(i,j,dist+1)
                dist += 1                    
                cur_set = temp_set
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    set_room(i, j)
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        if not rooms or not rooms[0]:
            return
        m, n = len(rooms), len(rooms[0])
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        def get_adjs(x, y, dist):
            res = set()
            for di, dj in dirs:
                i, j = di + x, dj + y
                if i >=0 and i < m and j >= 0 and j < n \
                        and rooms[i][j] > dist:
                    res.add((i,j))
            return res
        cur_set = set()
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    cur_set |= get_adjs(i,j,1) 
        dist = 1
        while cur_set:
            temp_set = set()
            # print(dist,cur_set)
            for i, j in cur_set:
                rooms[i][j] = dist
                temp_set |= get_adjs(i,j,dist+1)
            dist += 1
            cur_set = temp_set - cur_set