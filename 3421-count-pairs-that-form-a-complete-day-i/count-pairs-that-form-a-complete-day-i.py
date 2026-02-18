class Solution:
    def countCompleteDayPairs(self, hours):
        cnt = [0] * 24
        ans = 0

        for h in hours:
            r = h % 24
            need = (24 - r) % 24
            ans += cnt[need]
            cnt[r] += 1

        return ans
