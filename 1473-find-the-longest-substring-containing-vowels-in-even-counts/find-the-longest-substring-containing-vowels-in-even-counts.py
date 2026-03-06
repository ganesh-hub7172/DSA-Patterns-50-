class Solution:
    def findTheLongestSubstring(self, s):
        pos = {0: -1}
        mask = 0
        res = 0

        for i, ch in enumerate(s):
            if ch == 'a':
                mask ^= 1
            elif ch == 'e':
                mask ^= 2
            elif ch == 'i':
                mask ^= 4
            elif ch == 'o':
                mask ^= 8
            elif ch == 'u':
                mask ^= 16

            if mask in pos:
                res = max(res, i - pos[mask])
            else:
                pos[mask] = i

        return res