class Solution(object):
    def partitionString(self, s):
        seen = set()
        count = 1
        
        for ch in s:
            if ch in seen:
                count += 1
                seen.clear()
            seen.add(ch)
        
        return count
