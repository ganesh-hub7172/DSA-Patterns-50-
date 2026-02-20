class Solution:
    def sumDivisibleByK(self, nums, k):
        from collections import Counter
        
        freq = Counter(nums)
        total = 0
        
        for num in nums:
            if freq[num] % k == 0:
                total += num
                
        return total
