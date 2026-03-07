class Solution:
    def findCommonResponse(self, responses):
        freq = {}
        
        for day in responses:
            unique = set(day)
            for r in unique:
                freq[r] = freq.get(r, 0) + 1
        
        max_count = 0
        ans = ""
        
        for r in freq:
            if freq[r] > max_count or (freq[r] == max_count and r < ans):
                max_count = freq[r]
                ans = r
        
        return ans