class Solution:
    def getMaximumXor(self, nums, maximumBit):
        x = 0
        for v in nums:
            x ^= v
        
        mask = (1 << maximumBit) - 1
        ans = []
        
        for v in reversed(nums):
            ans.append(mask ^ x)
            x ^= v
        
        return ans
