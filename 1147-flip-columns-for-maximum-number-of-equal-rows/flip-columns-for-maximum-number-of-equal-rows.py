class Solution:
    def maxEqualRowsAfterFlips(self, matrix):
        from collections import Counter
        cnt = Counter()
        
        for row in matrix:
            if row[0] == 1:
                key = tuple(1 - x for x in row)
            else:
                key = tuple(row)
            cnt[key] += 1
        
        return max(cnt.values())
