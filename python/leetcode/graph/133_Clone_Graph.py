# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node: return None
        mem = {}
        def dfs(cur):
            if cur.label not in mem:
                mem[cur.label] = UndirectedGraphNode(cur.label)
                for child in cur.neighbors:
                    if child.label in mem:
                        mem[cur.label].neighbors += mem[child.label],
                    else:
                        mem[cur.label].neighbors += dfs(child),
            
            return mem[cur.label]
        return dfs(node)
    def cloneGraph(self, node):
        if not node: return None
        mem = {}
        q = [node]
        while q:
            cur = q.pop(0)
            if cur.label not in mem:
                mem[cur.label] = UndirectedGraphNode(cur.label)
            for child in cur.neighbors:
                if child.label not in mem:
                    mem[child.label] = UndirectedGraphNode(child.label)
                    q += child,
                mem[cur.label].neighbors += mem[child.label],
        return mem[node.label]
                