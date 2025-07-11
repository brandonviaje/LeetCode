from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        Notes:
        - w
        """
        queue = deque()
        fresh = 0
        min_minutes = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    continue
                elif grid[i][j] == 2:
                    queue.append((i, j))
                else:
                    fresh += 1
        
        if fresh == 0:
            return 0
        """
        fresh = 1
        [(0,1)]
        row = 0
        col = 1
        
        
        """
        
        while queue and fresh > 0:
            
            for _ in range(len(queue)):
                row,col = queue.popleft()
                print(row, col)
                
                neighbs = [
                    (row -1 , col),
                    (row + 1, col),
                    (row, col - 1),
                    (row, col + 1)
                ]
               
                for neighb_row,neighb_col in neighbs:
                    # boundary checks and also check if its a fresh orange
                    if 0 <= neighb_row < len(grid) and 0<=neighb_col<len(grid[0]) and grid[neighb_row][neighb_col] == 1:
                        grid[neighb_row][neighb_col] = 2
                        fresh -= 1
                        queue.append((neighb_row,neighb_col))
        
            min_minutes += 1
        

        if fresh > 0:
            return -1
        
        return min_minutes
        