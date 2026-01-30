class Solution:
    def findTheWinner(self, n, k):
        winner = 0  # 0-indexed
        for i in range(2, n + 1):
            winner = (winner + k) % i
        return winner + 1  # convert to 1-indexed
