class Solution:
    def countLargestGroup(self, n):
        groups = {}
        
        for i in range(1, n + 1):
            s = sum(int(d) for d in str(i))
            groups[s] = groups.get(s, 0) + 1
        
        max_size = max(groups.values())
        
        count = 0
        for v in groups.values():
            if v == max_size:
                count += 1
        
        return count