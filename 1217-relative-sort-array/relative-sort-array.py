class Solution:
    def relativeSortArray(self, arr1, arr2):
        freq = {}
        
        for num in arr1:
            freq[num] = freq.get(num, 0) + 1
        
        res = []
        
        for num in arr2:
            res += [num] * freq[num]
            del freq[num]
        
        remaining = []
        
        for num in freq:
            remaining += [num] * freq[num]
        
        remaining.sort()
        
        return res + remaining