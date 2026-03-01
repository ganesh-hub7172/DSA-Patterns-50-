class Solution:
    def isSumEqual(self, firstWord, secondWord, targetWord):
        
        def word_to_number(word):
            num_str = ""
            for ch in word:
                num_str += str(ord(ch) - ord('a'))
            return int(num_str)
        
        return word_to_number(firstWord) + word_to_number(secondWord) == word_to_number(targetWord)