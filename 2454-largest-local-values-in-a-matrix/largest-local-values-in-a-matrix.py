class Solution:
    def largestLocal(self, grid):
        n = len(grid)
        result = []

        for i in range(n - 2):
            row = []
            for j in range(n - 2):
                max_val = 0
                for r in range(i, i + 3):
                    for c in range(j, j + 3):
                        max_val = max(max_val, grid[r][c])
                row.append(max_val)
            result.append(row)

        return result
