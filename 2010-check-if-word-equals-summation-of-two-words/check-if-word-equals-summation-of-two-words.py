class Solution:
    def isSumEqual(self, firstWord, secondWord, targetWord):
        
        def getValue(word):
            num = ""
            for ch in word:
                num += str(ord(ch) - ord('a'))
            return int(num)
        
        return getValue(firstWord) + getValue(secondWord) == getValue(targetWord)