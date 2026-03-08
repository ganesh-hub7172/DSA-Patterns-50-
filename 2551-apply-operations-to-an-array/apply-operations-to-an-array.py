class Solution:
    def applyOperations(self, nums):
        n = len(nums)

        # Step 1: Apply operations
        for i in range(n - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0

        # Step 2: Move zeros to end
        res = []
        zeros = 0

        for num in nums:
            if num == 0:
                zeros += 1
            else:
                res.append(num)

        res.extend([0] * zeros)
        return res