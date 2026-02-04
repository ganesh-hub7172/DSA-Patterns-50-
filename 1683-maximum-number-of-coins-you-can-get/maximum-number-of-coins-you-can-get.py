class Solution:
    def maxCoins(self, piles):
        piles.sort()
        n = len(piles) // 3
        ans = 0
        j = len(piles) - 2
        for _ in range(n):
            ans += piles[j]
            j -= 2
        return ans
