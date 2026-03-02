class Solution:
    def countStableSubsequences(self, nums):
        MOD = 10**9 + 7
        
        dp_even_1 = dp_even_2 = 0
        dp_odd_1 = dp_odd_2 = 0
        
        for num in nums:
            if num % 2 == 0:
                new_even_1 = 1 + dp_odd_1 + dp_odd_2
                new_even_2 = dp_even_1
                
                dp_even_1 = (dp_even_1 + new_even_1) % MOD
                dp_even_2 = (dp_even_2 + new_even_2) % MOD
            
            else:
                new_odd_1 = 1 + dp_even_1 + dp_even_2
                new_odd_2 = dp_odd_1
                
                dp_odd_1 = (dp_odd_1 + new_odd_1) % MOD
                dp_odd_2 = (dp_odd_2 + new_odd_2) % MOD
        
        return (dp_even_1 + dp_even_2 + dp_odd_1 + dp_odd_2) % MOD