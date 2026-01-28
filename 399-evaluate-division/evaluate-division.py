from collections import defaultdict

class Solution:
    def calcEquation(self, equations, values, queries):
        graph = defaultdict(list)

        # Build graph
        for (a, b), val in zip(equations, values):
            graph[a].append((b, val))
            graph[b].append((a, 1 / val))

        def dfs(curr, target, visited):
            if curr == target:
                return 1.0

            visited.add(curr)

            for nei, weight in graph[curr]:
                if nei not in visited:
                    res = dfs(nei, target, visited)
                    if res != -1.0:
                        return res * weight

            return -1.0

        results = []
        for c, d in queries:
            if c not in graph or d not in graph:
                results.append(-1.0)
            else:
                results.append(dfs(c, d, set()))

        return results
