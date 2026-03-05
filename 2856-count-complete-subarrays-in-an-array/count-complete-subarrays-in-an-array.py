class Solution:
    def countCompleteSubarrays(self, nums):
        from collections import defaultdict
        
        n = len(nums)
        total_distinct = len(set(nums))
        
        freq = defaultdict(int)
        left = 0
        count = 0
        answer = 0
        
        for right in range(n):
            freq[nums[right]] += 1
            if freq[nums[right]] == 1:
                count += 1
            
            while count == total_distinct:
                answer += (n - right)
                
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    count -= 1
                left += 1
        
        return answer