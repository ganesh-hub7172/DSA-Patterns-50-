class Solution:
    def countCompleteComponents(self, n, edges):
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        seen = [False] * n

        def dfs(start):
            stack = [start]
            seen[start] = True
            nodes = []
            edge_sum = 0

            while stack:
                u = stack.pop()
                nodes.append(u)
                edge_sum += len(adj[u])
                for v in adj[u]:
                    if not seen[v]:
                        seen[v] = True
                        stack.append(v)

            k = len(nodes)
            return edge_sum // 2 == k * (k - 1) // 2

        ans = 0
        for i in range(n):
            if not seen[i]:
                if dfs(i):
                    ans += 1
        return ans
