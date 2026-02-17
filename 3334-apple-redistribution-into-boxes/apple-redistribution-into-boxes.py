class Solution(object):
    def minimumBoxes(self, apple, capacity):
        total = sum(apple)
        capacity.sort(reverse=True)
        
        used = 0
        cur = 0
        for c in capacity:
            cur += c
            used += 1
            if cur >= total:
                return used
        return used
