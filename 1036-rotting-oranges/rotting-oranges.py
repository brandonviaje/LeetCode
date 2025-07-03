from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh = 0

        # queue all rotten oranges, count fresh
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        # no fresh oranges, return 0
        if fresh == 0:
            return 0

        minutes = 0
        directions = [(-1,0), (1,0), (0,-1), (0,1)]

        # BFS
        while queue and fresh > 0:
            # process current level
            for _ in range(len(queue)):  
                r, c = queue.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    # bounds check, and check if it its fresh
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2 # change in place
                        fresh -= 1 # decrease fresh count
                        queue.append((nr, nc)) # add to queue to explore the next

            minutes += 1  

        if fresh == 0:
            return minutes 
        else: # else theres still fresh oranges that can go rotten
            return -1