class Solution:
    def findRedundantConnection(self, edges):
        parent = {}

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px = find(x)
            py = find(y)
            if px == py:
                return False
            parent[py] = px
            return True

        for u, v in edges:
            if u not in parent:
                parent[u] = u
            if v not in parent:
                parent[v] = v

            if not union(u, v):
                return [u, v]
