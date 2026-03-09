class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                # check if equal to cell belo
                if row + 1 < len(grid) and grid[row][col] != grid[row+1][col]:
                    return False
                
                if col + 1 < len(grid[0]) and grid[row][col] == grid[row][col+1]:
                    return False

        return True