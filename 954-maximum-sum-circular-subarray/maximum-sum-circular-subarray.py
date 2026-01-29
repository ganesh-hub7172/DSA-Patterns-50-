class Solution:
    def maxSubarraySumCircular(self, nums):
        total = sum(nums)

        # Standard Kadane's algorithm for max subarray
        max_kadane = curr_max = nums[0]
        for num in nums[1:]:
            curr_max = max(num, curr_max + num)
            max_kadane = max(max_kadane, curr_max)

        # Modified Kadane's for min subarray
        min_kadane = curr_min = nums[0]
        for num in nums[1:]:
            curr_min = min(num, curr_min + num)
            min_kadane = min(min_kadane, curr_min)

        max_circular = total - min_kadane

        # Handle case where all numbers are negative
        if max_circular == 0:
            return max_kadane

        return max(max_kadane, max_circular)

