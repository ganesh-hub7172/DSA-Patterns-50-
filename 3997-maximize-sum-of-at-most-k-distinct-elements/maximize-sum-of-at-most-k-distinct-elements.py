class Solution:
    def maxKDistinct(self, nums, k):
        # Remove duplicates
        unique_nums = list(set(nums))
        
        # Sort in descending order
        unique_nums.sort(reverse=True)
        
        # Return at most k elements
        return unique_nums[:k]