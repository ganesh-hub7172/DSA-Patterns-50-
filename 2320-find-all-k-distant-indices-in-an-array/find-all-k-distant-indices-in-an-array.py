class Solution:
    def findKDistantIndices(self, nums, key, k):
        n = len(nums)
        result = set()
        
        for j in range(n):
            if nums[j] == key:
                left = max(0, j - k)
                right = min(n - 1, j + k)
                for i in range(left, right + 1):
                    result.add(i)
        
        return sorted(result)
