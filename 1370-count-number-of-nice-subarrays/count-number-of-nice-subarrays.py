class Solution:
    def numberOfSubarrays(self, nums, k):
        prefix = {0:1}
        count = 0
        odd = 0
        
        for num in nums:
            if num % 2 == 1:
                odd += 1
            
            if odd - k in prefix:
                count += prefix[odd - k]
            
            prefix[odd] = prefix.get(odd, 0) + 1
        
        return count