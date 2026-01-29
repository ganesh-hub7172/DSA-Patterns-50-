class Solution:
    def balancedStringSplit(self, s):
        count = 0
        balance = 0

        for ch in s:
            if ch == 'R':
                balance += 1
            else:  # 'L'
                balance -= 1

            if balance == 0:
                count += 1

        return count
