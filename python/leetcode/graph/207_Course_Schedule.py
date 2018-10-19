class Solution(object):
    def canFinish(self, num_courses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if num_courses <= 1:
            return True
        depend_list = [[] for _ in xrange(num_courses)]
        back_list = [[] for _ in xrange(num_courses)]
        for i,j in prerequisites:
            depend_list[i].append(j)
            back_list[j].append(i)
        leaves = [i for i in xrange(num_courses) if len(depend_list[i])==0]
        while len(leaves) > 0:
            new_leaves = []
            for leave_i in leaves:
                for back_j in back_list[leave_i]:
                    depend_list[back_j].remove(leave_i)
                    if len(depend_list[back_j]) == 0: 
                        new_leaves.append(back_j)
                back_list[leave_i] = []
            leaves = new_leaves
        for depend in depend_list:
            if len(depend) >0 :
                return False
        return True

    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        from collections import defaultdict
        mem = defaultdict(list)
        visited, handled = set(), set()
        for src, dst in prerequisites:
            mem[src] += dst,
        def dfs(src):
            handled.add(src)
            visited.add(src)
            for i in mem[src]:
                if i in visited:
                    return False
                else:
                    if i not in handled:
                        if not dfs(i):
                            return False
            visited.discard(src)
            return True
        for i in range(numCourses):
            if i not in handled:
                if not dfs(i):
                    return False
        return True
    # bad performance
    def canFinish(self, n, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        matrix = [ [0] * n for _ in range(n)]                
        in_degrees = [0] * n
        for src, dst in prerequisites:
            matrix[dst][src] = 1
            in_degrees[src] += 1
        count, q = 0, []
        for i in range(n):
            if in_degrees[i] == 0: 
                q += i,
        while q:
            dst = q.pop(0)
            count += 1
            for i in range(n):
                if matrix[dst][i]>0:
                    in_degrees[i] -= 1
                    if in_degrees[i] == 0:
                        q += i,
        count.p()
        return count == n
# public boolean canFinish(int numCourses, int[][] prerequisites) {
#     int[][] matrix = new int[numCourses][numCourses]; // i -> j
#     int[] indegree = new int[numCourses];
    
#     for (int i=0; i<prerequisites.length; i++) {
#         int ready = prerequisites[i][0];
#         int pre = prerequisites[i][1];
#         if (matrix[pre][ready] == 0)
#             indegree[ready]++; //duplicate case
#         matrix[pre][ready] = 1;
#     }
    
#     int count = 0;
#     Queue<Integer> queue = new LinkedList();
#     for (int i=0; i<indegree.length; i++) {
#         if (indegree[i] == 0) queue.offer(i);
#     }
#     while (!queue.isEmpty()) {
#         int course = queue.poll();
#         count++;
#         for (int i=0; i<numCourses; i++) {
#             if (matrix[course][i] != 0) {
#                 if (--indegree[i] == 0)
#                     queue.offer(i);
#             }
#         }
#     }
#     return count == numCourses;
# }        

if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        Solution().canFinish(2,[[1,0]]).must_equal(True)
        Solution().canFinish(3,[[0,1],[0,2],[1,2]]).must_equal(True)

