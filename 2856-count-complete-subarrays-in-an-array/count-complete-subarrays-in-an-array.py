class Solution:
    def countCompleteSubarrays(self, nums):
        k = len(set(nums))
        freq = {}
        left = 0
        count = 0

        for right in range(len(nums)):
            freq[nums[right]] = freq.get(nums[right], 0) + 1

            while len(freq) == k:
                count += len(nums) - right
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    del freq[nums[left]]
                left += 1

        return count