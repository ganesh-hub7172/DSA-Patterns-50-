class Solution:
    def regionsBySlashes(self, grid):
        n = len(grid)
        size = n * 3
        mat = [[0] * size for _ in range(size)]

        for i in range(n):
            for j in range(n):
                c = grid[i][j]
                if c == '/':
                    mat[i*3+0][j*3+2] = 1
                    mat[i*3+1][j*3+1] = 1
                    mat[i*3+2][j*3+0] = 1
                elif c == '\\':
                    mat[i*3+0][j*3+0] = 1
                    mat[i*3+1][j*3+1] = 1
                    mat[i*3+2][j*3+2] = 1

        def dfs(r, c):
            if r < 0 or c < 0 or r >= size or c >= size or mat[r][c] != 0:
                return
            mat[r][c] = 1
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        ans = 0
        for i in range(size):
            for j in range(size):
                if mat[i][j] == 0:
                    ans += 1
                    dfs(i, j)

        return ans
