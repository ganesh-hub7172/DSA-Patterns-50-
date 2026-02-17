class Solution(object):
    def minTimeToType(self, word):
        cur = 0
        ans = 0
        
        for ch in word:
            target = ord(ch) - ord('a')
            diff = abs(target - cur)
            ans += min(diff, 26 - diff) + 1
            cur = target
        
        return ans
