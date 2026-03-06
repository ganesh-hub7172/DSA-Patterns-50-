class Solution:
    def uncommonFromSentences(self, s1, s2):
        freq = {}
        
        for word in (s1 + " " + s2).split():
            freq[word] = freq.get(word, 0) + 1
        
        res = []
        for word in freq:
            if freq[word] == 1:
                res.append(word)
        
        return res