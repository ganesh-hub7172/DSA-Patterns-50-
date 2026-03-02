class Solution:
    def mapWordWeights(self, words, weights):
        result = []
        
        for word in words:
            total_weight = 0
            
            for ch in word:
                total_weight += weights[ord(ch) - ord('a')]
            
            mod = total_weight % 26
            
            # Reverse alphabetical mapping
            mapped_char = chr(ord('z') - mod)
            result.append(mapped_char)
        
        return "".join(result)