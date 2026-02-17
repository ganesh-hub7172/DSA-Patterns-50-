class Solution(object):
    def minimumArea(self, grid):
        min_r = float('inf')
        max_r = -1
        min_c = float('inf')
        max_c = -1

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    if r < min_r:
                        min_r = r
                    if r > max_r:
                        max_r = r
                    if c < min_c:
                        min_c = c
                    if c > max_c:
                        max_c = c

        if max_r == -1:
            return 0

        return (max_r - min_r + 1) * (max_c - min_c + 1)
