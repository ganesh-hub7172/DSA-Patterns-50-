class Solution(object):
    def minSwaps(self, s):
        balance = 0
        min_balance = 0
        
        for ch in s:
            if ch == '[':
                balance += 1
            else:
                balance -= 1
            if balance < min_balance:
                min_balance = balance
        
        return (-min_balance + 1) // 2
