class Solution:
    def sumOddLengthSubarrays(self, arr):
        n = len(arr)
        ans = 0
        for i, x in enumerate(arr):
            total = (i + 1) * (n - i)
            ans += ((total + 1) // 2) * x
        return ans
