from collections import deque

class Solution:
    def maxResult(self, nums, k):
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]

        q = deque()
        q.append(0)

        for i in range(1, n):
            # Remove indices outside the window
            while q and q[0] < i - k:
                q.popleft()

            # dp[i] = nums[i] + max(dp[j]) in the window
            dp[i] = nums[i] + dp[q[0]]

            # Maintain deque in decreasing order of dp values
            while q and dp[i] >= dp[q[-1]]:
                q.pop()

            q.append(i)

        return dp[-1]
