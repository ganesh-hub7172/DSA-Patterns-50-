class Solution:
    def maxValue(self, n, x):
        x = str(x)
        
        # If number is negative
        if n[0] == '-':
            for i in range(1, len(n)):
                if n[i] > x:
                    return n[:i] + x + n[i:]
            return n + x
        
        # If number is positive
        else:
            for i in range(len(n)):
                if n[i] < x:
                    return n[:i] + x + n[i:]
            return n + x