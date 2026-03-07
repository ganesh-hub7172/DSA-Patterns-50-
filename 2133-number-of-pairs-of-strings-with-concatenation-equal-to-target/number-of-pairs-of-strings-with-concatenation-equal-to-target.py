class Solution:
    def numOfPairs(self, nums, target):
        freq = {}
        
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        count = 0
        
        for a in nums:
            if target.startswith(a):
                b = target[len(a):]
                
                if b in freq:
                    count += freq[b]
                    
                    if a == b:
                        count -= 1
        
        return count