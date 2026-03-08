from collections import Counter

class Solution:
    def commonChars(self, words):
        common = Counter(words[0])
        
        for word in words[1:]:
            common &= Counter(word)
        
        res = []
        for char, count in common.items():
            res.extend([char] * count)
        
        return res