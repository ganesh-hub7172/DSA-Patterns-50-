class Solution:
    def findRedundantDirectedConnection(self, edges):
        n = len(edges)
        parent = list(range(n + 1))
        indegree = [0] * (n + 1)

        # Step 1: find node with two parents
        cand1 = None
        cand2 = None

        for u, v in edges:
            if indegree[v] == 0:
                indegree[v] = u
            else:
                # v has two parents
                cand1 = [indegree[v], v]
                cand2 = [u, v]
                break

        # Union-Find helpers
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

        # Step 2: try union, skipping cand2 if exists
        parent = list(range(n + 1))
        for u, v in edges:
            if [u, v] == cand2:
                continue
            if not union(u, v):
                # cycle detected
                if cand1:
                    return cand1
                return [u, v]

        # Step 3: no cycle, return second parent edge
        return cand2
