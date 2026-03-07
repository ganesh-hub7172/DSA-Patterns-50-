class Solution:
    def largestSubmatrix(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        
        for i in range(1, m):
            for j in range(n):
                if matrix[i][j] == 1:
                    matrix[i][j] += matrix[i-1][j]
        
        res = 0
        
        for row in matrix:
            row_sorted = sorted(row, reverse=True)
            
            for j in range(n):
                area = row_sorted[j] * (j + 1)
                res = max(res, area)
        
        return res