class Solution:
    def generateKey(self, num1, num2, num3):
        a = str(num1).zfill(4)
        b = str(num2).zfill(4)
        c = str(num3).zfill(4)
        
        result = ""
        
        for i in range(4):
            result += str(min(a[i], b[i], c[i]))
        
        return int(result)