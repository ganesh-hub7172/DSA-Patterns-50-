class Solution:
    def minMaxDifference(self, num):
        s = str(num)
        
        # For maximum
        max_s = s
        for ch in s:
            if ch != '9':
                max_s = s.replace(ch, '9')
                break
        
        # For minimum
        min_s = s.replace(s[0], '0')
        
        return int(max_s) - int(min_s)