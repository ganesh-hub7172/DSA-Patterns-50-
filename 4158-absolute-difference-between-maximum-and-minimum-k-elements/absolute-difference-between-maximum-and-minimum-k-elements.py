class Solution:
    def absDifference(self, nums, k):
        nums.sort()
        
        smallest_sum = sum(nums[:k])
        largest_sum = sum(nums[-k:])
        
        return abs(largest_sum - smallest_sum)