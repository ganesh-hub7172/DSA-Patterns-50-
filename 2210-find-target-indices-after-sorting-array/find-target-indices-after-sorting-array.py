class Solution:
    def targetIndices(self, nums, target):
        nums.sort()
        return [i for i, v in enumerate(nums) if v == target]
