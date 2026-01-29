class Solution:
    def firstUniqChar(self, s):
        # Step 1: Count frequency of each character
        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1
        
        # Step 2: Find the first character with frequency 1
        for i, char in enumerate(s):
            if freq[char] == 1:
                return i
        
        # Step 3: If no unique character found
        return -1

# Example usage
s = "leetcode"
ret = Solution().firstUniqChar(s)
print(ret)  # Output: 0
