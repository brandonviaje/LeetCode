class Solution:
    def DFS(self,grid,row,col,seen):

        stack = [(row,col)]
        seen.add((row,col))
        area = 1

        while stack:
            cand_row,cand_col = stack.pop()

            neighbs = [
                (cand_row -1,cand_col),
                (cand_row + 1,cand_col),
                (cand_row,cand_col -1),
                (cand_row,cand_col + 1)
            ]

            for neighb_row,neighb_col in neighbs:
                # check out of bounds, seen and is not water
                if 0 <= neighb_row < len(grid) and 0<= neighb_col < len(grid[0]) and (neighb_row,neighb_col) not in seen and grid[neighb_row][neighb_col] != 0:
                    stack.append((neighb_row,neighb_col))
                    seen.add((neighb_row,neighb_col))
                    area += 1

        return area

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        seen = set()
        maxArea = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    area = self.DFS(grid,row,col,seen) #DFS to find area of that island
                    maxArea = max(maxArea,area) # update max area

        return maxArea