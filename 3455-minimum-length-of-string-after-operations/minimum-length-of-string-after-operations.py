class Solution:
    def minimumLength(self, s):
        freq = {}
        
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1
        
        res = 0
        
        for f in freq.values():
            if f % 2 == 0:
                res += 2
            else:
                res += 1
        
        return res