class Solution(object):
    def minLengthAfterRemovals(self, s):
        a = s.count('a')
        b = s.count('b')
        return abs(a - b)
