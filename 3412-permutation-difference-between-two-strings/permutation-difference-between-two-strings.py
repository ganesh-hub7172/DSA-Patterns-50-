class Solution:
    def findPermutationDifference(self, s, t):
        pos = {}

        # Store index of each character in s
        for i, ch in enumerate(s):
            pos[ch] = i

        diff = 0
        for i, ch in enumerate(t):
            diff += abs(pos[ch] - i)

        return diff
