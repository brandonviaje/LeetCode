from collections import deque

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        
        rows = len(maze)
        cols = len(maze[0])
        queue = deque([(entrance[0],entrance[1],0)])
        seen = set([tuple(entrance)])

        while queue:
            
            # pop current row,col and step
            cand_row,cand_col,steps = queue.popleft()

            # check if player is at border and not at entrance
            if [cand_row,cand_col] != entrance and (cand_row == 0 or cand_row == rows - 1 or cand_col == 0 or cand_col == cols -1):
                return steps

            # process adjacent neighbs
            neighbs = [
                (cand_row - 1,cand_col),
                (cand_row + 1,cand_col),
                (cand_row,cand_col - 1),
                (cand_row,cand_col + 1)
            ]

            for neighb_row,neighb_col in neighbs:
                # check for index bounds
                if neighb_row < 0 or neighb_row >= rows:
                    continue

                if neighb_col < 0 or neighb_col >= cols:
                    continue

                # continue if already visited
                if (neighb_row, neighb_col) in seen:
                    continue

                # continue if we its a wall 
                if maze[neighb_row][neighb_col] == '+':
                    continue

                # after passing all checks, add valid node and increment step
                queue.append((neighb_row,neighb_col,steps + 1))
                seen.add((neighb_row,neighb_col)) 

        return -1

        # T  O(rows * cols) S O(rows * cols)