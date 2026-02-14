class Solution:
    def countKConstraintSubstrings(self, s, k):
        n = len(s)
        left = zeros = ones = res = 0
        
        for right in range(n):
            if s[right] == '0':
                zeros += 1
            else:
                ones += 1
            
            while zeros > k and ones > k:
                if s[left] == '0':
                    zeros -= 1
                else:
                    ones -= 1
                left += 1
            
            res += right - left + 1
        
        return res
