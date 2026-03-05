class Solution:
    def maximumStrongPairXor(self, nums):
        nums.sort()
        n = len(nums)
        max_xor = 0
        
        for i in range(n):
            for j in range(i, n):
                if nums[j] <= 2 * nums[i]:
                    max_xor = max(max_xor, nums[i] ^ nums[j])
                else:
                    break
        
        return max_xor