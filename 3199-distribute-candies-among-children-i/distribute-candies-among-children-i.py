class Solution:
    def distributeCandies(self, n, limit):
        def comb2(x):
            if x < 0:
                return 0
            return (x + 2) * (x + 1) // 2
        
        L = limit + 1
        
        return (
            comb2(n)
            - 3 * comb2(n - L)
            + 3 * comb2(n - 2 * L)
            - comb2(n - 3 * L)
        )