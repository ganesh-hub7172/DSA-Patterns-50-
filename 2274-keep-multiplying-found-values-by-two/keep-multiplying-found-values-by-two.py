class Solution:
    def findFinalValue(self, nums, original):
        s = set(nums)
        
        while original in s:
            original = original * 2
        
        return original