from collections import defaultdict, deque

class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))

        dist = [float('inf')] * n
        dist[src] = 0

        queue = deque([(src, 0)])
        stops = 0

        while queue and stops <= k:
            size = len(queue)
            temp_dist = dist[:]

            for _ in range(size):
                node, cost = queue.popleft()

                for nei, price in graph[node]:
                    if cost + price < temp_dist[nei]:
                        temp_dist[nei] = cost + price
                        queue.append((nei, temp_dist[nei]))

            dist = temp_dist
            stops += 1

        return -1 if dist[dst] == float('inf') else dist[dst]
