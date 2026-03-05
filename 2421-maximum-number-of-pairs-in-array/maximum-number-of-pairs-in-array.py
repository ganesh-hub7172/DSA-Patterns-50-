class Solution:
    def numberOfPairs(self, nums):
        from collections import Counter
        
        freq = Counter(nums)
        
        pairs = 0
        leftovers = 0
        
        for f in freq.values():
            pairs += f // 2
            leftovers += f % 2
        
        return [pairs, leftovers]