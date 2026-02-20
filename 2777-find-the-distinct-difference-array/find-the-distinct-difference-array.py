class Solution:
    def distinctDifferenceArray(self, nums):
        n = len(nums)
        diff = [0] * n
        
        prefix_set = set()
        suffix_count = {}
        
        for num in nums:
            suffix_count[num] = suffix_count.get(num, 0) + 1
        
        for i in range(n):
            prefix_set.add(nums[i])
            suffix_count[nums[i]] -= 1
            if suffix_count[nums[i]] == 0:
                del suffix_count[nums[i]]
            
            diff[i] = len(prefix_set) - len(suffix_count)
        
        return diff
