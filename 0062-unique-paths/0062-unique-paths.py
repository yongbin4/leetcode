class Solution:
    def uniquePaths(self, rows: int, columns: int) -> int:
        grid = [[1]*columns] * rows
        
        for row in range(1, rows):
            for column in range(1, columns):
                grid[row][column] = grid[row - 1][column] + grid[row][column - 1]
        
        return grid[rows - 1][columns - 1]
        