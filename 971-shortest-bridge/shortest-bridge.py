class Solution:

    def DFS(self,grid,row,col,seen):

        stack = [(row,col)]
        seen.add((row, col))

        while stack:
            # process current node
            cand_row,cand_col = stack.pop()

            neighbs = [
                (cand_row - 1,cand_col),
                (cand_row + 1,cand_col),
                (cand_row,cand_col - 1),
                (cand_row,cand_col + 1)
            ]

            for neighb_row,neighb_col in neighbs:
                # check out of bounds , not in seen, and is land node
                if 0 <= neighb_row < len(grid) and 0 <= neighb_col < len(grid[0]) and (neighb_row,neighb_col) not in seen and grid[neighb_row][neighb_col] != 0:
                    stack.append((neighb_row,neighb_col))
                    seen.add((neighb_row,neighb_col))

    def BFS(self,grid,seen):

        queue = deque(seen)
        shortestPath = 0

        while queue:
            # go level by level
            for _ in range(len(queue)):
                # process current node
                cand_row,cand_col = queue.popleft()

                neighbs = [
                    (cand_row - 1,cand_col),
                    (cand_row + 1,cand_col),
                    (cand_row,cand_col - 1),
                    (cand_row,cand_col + 1)
                ]

                for neighb_row,neighb_col in neighbs:
                    # out of bounds and check if in set
                    if 0 <= neighb_row <len(grid) and 0 <= neighb_col <len(grid[0]) and (neighb_row,neighb_col) not in seen:
                        if grid[neighb_row][neighb_col] == 1:
                            return shortestPath

                        seen.add((neighb_row,neighb_col))
                        queue.append((neighb_row, neighb_col))
                
            shortestPath += 1 # add 1 after each level

    def shortestBridge(self, grid: List[List[int]]) -> int:

        seen = set()

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    self.DFS(grid,row,col,seen) # DFS to find all first island cells
                    return self.BFS(grid,seen) # BFS on first island cells to find shortest path
            
    # T O(n^2) S O(n^2)