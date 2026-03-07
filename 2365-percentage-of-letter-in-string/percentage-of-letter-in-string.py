class Solution:
    def percentageLetter(self, s, letter):
        count = 0
        
        for ch in s:
            if ch == letter:
                count += 1
        
        return (count * 100) // len(s)