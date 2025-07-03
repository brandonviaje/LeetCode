class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        """
        if the cells neighbours dont have a 1, add to it because thats the outside
        """

        def countSides(cand_row,cand_col):

            total = 0
            neighbs = [
                (cand_row-1,cand_col),
                (cand_row,cand_col+1),
                (cand_row+1,cand_col),
                (cand_row,cand_col-1),
            ]

            for neighb_row,neighb_col in neighbs:
                # if adjacent neighbour is in bounds and is land, dont add 
                if 0<= neighb_row<len(grid) and 0<=neighb_col<len(grid[0]) and grid[neighb_row][neighb_col] == 1:
                    continue
                else: # u are at water or the edge so add
                    total += 1
            return total
        
        perimeter = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                # if encounter land get the perimeter of that cell and add
                if grid[row][col] == 1:
                    perimeter += countSides(row,col)
        
        return perimeter

        