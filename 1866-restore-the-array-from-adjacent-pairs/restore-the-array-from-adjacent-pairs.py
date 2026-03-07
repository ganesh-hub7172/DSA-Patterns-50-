class Solution:
    def restoreArray(self, adjacentPairs):
        graph = {}
        
        for u, v in adjacentPairs:
            graph.setdefault(u, []).append(v)
            graph.setdefault(v, []).append(u)
        
        start = None
        for node in graph:
            if len(graph[node]) == 1:
                start = node
                break
        
        res = [start]
        prev = None
        
        while len(res) < len(graph):
            curr = res[-1]
            for nei in graph[curr]:
                if nei != prev:
                    res.append(nei)
                    prev = curr
                    break
        
        return res