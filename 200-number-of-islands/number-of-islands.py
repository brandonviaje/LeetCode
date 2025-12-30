class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        def DFS(row,col):
            # set as seen
            grid[row][col] = "0"
            stack = [(row,col)]

            # run dfs while stack has stuff to process still
            while stack:
                cr,cc = stack.pop()
                # iterate through neighbors, add to stack to process them even further
                for neighb_row, neighb_col in [(cr+1,cc),(cr-1,cc),(cr,cc+1),(cr,cc-1)]:
            
                    # bounds check, also check if neighboring cell is a land cell
                    if 0<=neighb_row<ROWS and 0<=neighb_col<COLS and grid[neighb_row][neighb_col] == "1":
                        # add to stack to process even further
                        stack.append((neighb_row,neighb_col))
                        # set as seen
                        grid[neighb_row][neighb_col] = "0"
     

        ROWS = len(grid)
        COLS = len(grid[0])
        islands = 0
        for i in range(ROWS):
            for j in range(COLS):
                # run a DFS so that you can add all the island cells
                if grid[i][j] == "1":
                    DFS(i,j)
                    islands += 1

        return islands