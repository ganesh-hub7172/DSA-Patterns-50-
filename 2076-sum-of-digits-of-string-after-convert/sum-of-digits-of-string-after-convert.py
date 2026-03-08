class Solution:
    def getLucky(self, s, k):
        num = ""
        
        for ch in s:
            num += str(ord(ch) - ord('a') + 1)
        
        for _ in range(k):
            total = 0
            for d in num:
                total += int(d)
            num = str(total)
        
        return int(num)