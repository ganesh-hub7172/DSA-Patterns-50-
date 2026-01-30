from collections import deque

class Solution:
    def eventualSafeNodes(self, graph):
        n = len(graph)
        outdegree = [0] * n
        reverse_graph = [[] for _ in range(n)]

        for u in range(n):
            outdegree[u] = len(graph[u])
            for v in graph[u]:
                reverse_graph[v].append(u)

        queue = deque()
        for i in range(n):
            if outdegree[i] == 0:
                queue.append(i)

        safe = [False] * n

        while queue:
            node = queue.popleft()
            safe[node] = True

            for prev in reverse_graph[node]:
                outdegree[prev] -= 1
                if outdegree[prev] == 0:
                    queue.append(prev)

        return [i for i in range(n) if safe[i]]
