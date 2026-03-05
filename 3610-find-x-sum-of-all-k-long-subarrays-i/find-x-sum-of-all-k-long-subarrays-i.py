class Solution:
    def findXSum(self, nums, k, x):
        from collections import Counter
        
        n = len(nums)
        answer = []
        
        for i in range(n - k + 1):
            window = nums[i:i+k]
            freq = Counter(window)
            
            # Sort by frequency desc, value desc
            sorted_elements = sorted(freq.items(), key=lambda item: (-item[1], -item[0]))
            
            total = 0
            count = 0
            
            for value, f in sorted_elements:
                if count < x:
                    total += value * f
                    count += 1
                else:
                    break
                    
            answer.append(total)
        
        return answer