class Solution:
    def largestMagicSquare(self, grid):
        m = len(grid)
        n = len(grid[0])
        
        def isMagic(r, c, k):
            diag1 = 0
            diag2 = 0
            
            for i in range(k):
                diag1 += grid[r+i][c+i]
                diag2 += grid[r+i][c+k-1-i]
            
            if diag1 != diag2:
                return False
            
            target = diag1
            
            for i in range(k):
                row_sum = 0
                col_sum = 0
                for j in range(k):
                    row_sum += grid[r+i][c+j]
                    col_sum += grid[r+j][c+i]
                
                if row_sum != target or col_sum != target:
                    return False
            
            return True
        
        max_k = min(m, n)
        
        for k in range(max_k, 0, -1):
            for r in range(m-k+1):
                for c in range(n-k+1):
                    if isMagic(r, c, k):
                        return k
        
        return 1