class Solution:
    def maxContainers(self, n, w, maxWeight):
        return min(n * n, maxWeight // w)