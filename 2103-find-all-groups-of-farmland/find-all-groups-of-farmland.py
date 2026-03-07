class Solution:
    def findFarmland(self, land):
        m = len(land)
        n = len(land[0])
        res = []
        
        for i in range(m):
            for j in range(n):
                if land[i][j] == 1:
                    if (i == 0 or land[i-1][j] == 0) and (j == 0 or land[i][j-1] == 0):
                        r = i
                        c = j
                        
                        while r < m and land[r][j] == 1:
                            r += 1
                        
                        while c < n and land[i][c] == 1:
                            c += 1
                        
                        res.append([i, j, r-1, c-1])
        
        return res