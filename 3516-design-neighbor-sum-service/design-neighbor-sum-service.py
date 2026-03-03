class NeighborSum:

    def __init__(self, grid):
        self.grid = grid
        self.n = len(grid)
        self.position = {}
        
        # Store value -> (row, col)
        for r in range(self.n):
            for c in range(self.n):
                self.position[grid[r][c]] = (r, c)

    def adjacentSum(self, value):
        r, c = self.position[value]
        total = 0
        
        # Up
        if r > 0:
            total += self.grid[r - 1][c]
        # Down
        if r < self.n - 1:
            total += self.grid[r + 1][c]
        # Left
        if c > 0:
            total += self.grid[r][c - 1]
        # Right
        if c < self.n - 1:
            total += self.grid[r][c + 1]
        
        return total

    def diagonalSum(self, value):
        r, c = self.position[value]
        total = 0
        
        # Top-left
        if r > 0 and c > 0:
            total += self.grid[r - 1][c - 1]
        # Top-right
        if r > 0 and c < self.n - 1:
            total += self.grid[r - 1][c + 1]
        # Bottom-left
        if r < self.n - 1 and c > 0:
            total += self.grid[r + 1][c - 1]
        # Bottom-right
        if r < self.n - 1 and c < self.n - 1:
            total += self.grid[r + 1][c + 1]
        
        return total