class Solution(object):
    def xorQueries(self, arr, queries):
        pref = [0]
        for x in arr:
            pref.append(pref[-1] ^ x)
        
        ans = []
        for l, r in queries:
            ans.append(pref[r + 1] ^ pref[l])
        return ans
