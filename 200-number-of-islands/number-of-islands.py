class Solution:

    def DFS(self,grid,seen,row,col):

        stack = [(row,col)]
        seen.add((row,col))

        while stack:
            cand_row,cand_col = stack.pop()

            # horizontal and vertically adjq
            neighbs = [
            (cand_row + 1,cand_col),
            (cand_row - 1,cand_col),
            (cand_row,cand_col + 1),
            (cand_row,cand_col - 1)
            ]

            for neighb_row, neighb_col in neighbs:

                # check for out of bounds
                if neighb_row < 0 or neighb_row >= len(grid):
                    continue

                if neighb_col < 0 or neighb_col >= len(grid[0]):
                    continue

                # if already seen
                if (neighb_row,neighb_col) in seen:
                    continue    

                # node hasn't been visited and is valid
                if grid[neighb_row][neighb_col] == "1":
                    stack.append((neighb_row,neighb_col))
                    seen.add((neighb_row,neighb_col))
                

    def numIslands(self, grid: List[List[str]]) -> int:
        result = 0
        # add a seen array to avoid inf loops when exploring 
        seen = set()

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                # check if we haven't seen this node yet and if it is land
                if grid[row][col] == "1" and (row,col) not in seen:
                    self.DFS(grid,seen,row,col) # DFS to explore valid adjacent nodes
                    result += 1

        return result