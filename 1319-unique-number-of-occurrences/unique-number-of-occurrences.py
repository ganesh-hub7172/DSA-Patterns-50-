class Solution:
    def uniqueOccurrences(self, arr):
        from collections import Counter
        c = Counter(arr)
        return len(set(c.values())) == len(c)
