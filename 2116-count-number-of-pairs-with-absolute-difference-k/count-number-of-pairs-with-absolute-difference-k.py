from collections import Counter

class Solution:
    def countKDifference(self, nums, k):
        freq = Counter()
        ans = 0
        
        for x in nums:
            ans += freq[x - k] + freq[x + k]
            freq[x] += 1
        
        return ans
