from collections import deque

class Solution:
    def findMinHeightTrees(self, n, edges):
        if n == 1:
            return [0]

        graph = [[] for _ in range(n)]
        degree = [0] * n

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
            degree[a] += 1
            degree[b] += 1

        queue = deque()
        for i in range(n):
            if degree[i] == 1:
                queue.append(i)

        remaining = n

        while remaining > 2:
            size = len(queue)
            remaining -= size

            for _ in range(size):
                node = queue.popleft()
                for nei in graph[node]:
                    degree[nei] -= 1
                    if degree[nei] == 1:
                        queue.append(nei)

        return list(queue)
