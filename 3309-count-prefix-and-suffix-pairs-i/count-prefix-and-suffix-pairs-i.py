class Solution:
    def countPrefixSuffixPairs(self, words):
        n = len(words)
        ans = 0
        for i in range(n):
            w = words[i]
            for j in range(i + 1, n):
                s = words[j]
                if s.startswith(w) and s.endswith(w):
                    ans += 1
        return ans
