class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        """
        count the number of islands by doing a DFS to explore all horizontally and vertically adjacent cells
        DFS for graphs using matrix would be O(m*n) as you have to iterate through the whole grid
        U can either keep track of the coords of each cell by using a set or overwriting it on the grid
        """

        # DFS so that we can mark all neighboring cells
        def DFS(row,col):
            # mark the starting point as seen
            grid[row][col] = "2"

            # stack for DFS
            stack = [(row,col)]

            # while the stack isnt empty, explore all neighboring cells and mark it as seen so you dont
            # encounter any infinite loops
            while stack:
                cand_row,cand_col = stack.pop()

                # neighboring cells can only be vertically and horizontally adjacent to each other
                neighbs = [
                    (cand_row - 1,cand_col),
                    (cand_row + 1,cand_col),
                    (cand_row,cand_col - 1),
                    (cand_row,cand_col + 1)
                ]

                # this would only be O(1) since you have a fixed size of 4 always
                for nr,nc in neighbs:
                    # what do we have to check for it?
                    # bounds check, check if its water or seen

                    if 0<=nr<ROWS and 0<=nc<COLS and grid[nr][nc] == "1":
                        # add cell to the stack to explore even further, then mark it as seen
                        stack.append((nr,nc))
                        grid[nr][nc] = "2"

        ROWS = len(grid)
        COLS = len(grid[0])
        islands = 0

        for row in range(ROWS):
            for col in range(COLS):
                # if its equal to 1, it is an unvisited island
                if grid[row][col] == "1":
                    DFS(row,col) # keep track of all valid islands cells thats part of the island rn
                    islands += 1 # iterate islands 

        return islands

        """
        [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]]
        """