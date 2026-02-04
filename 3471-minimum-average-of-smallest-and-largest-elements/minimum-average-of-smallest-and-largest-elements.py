class Solution:
    def minimumAverage(self, nums):
        nums.sort()
        i, j = 0, len(nums) - 1
        ans = float("inf")
        
        while i < j:
            ans = min(ans, (nums[i] + nums[j]) / 2.0)
            i += 1
            j -= 1
        
        return ans
