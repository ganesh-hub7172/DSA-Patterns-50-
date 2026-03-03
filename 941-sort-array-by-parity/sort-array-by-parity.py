class Solution:
    def sortArrayByParity(self, nums):
        evens = []
        odds = []
        
        for num in nums:
            if num % 2 == 0:
                evens.append(num)
            else:
                odds.append(num)
        
        return evens + odds