from collections import deque
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        ROWS = len(maze)
        COLS = len(maze[0])
        queue = deque([(entrance[0],entrance[1])])
        distance = 0
        maze[entrance[0]][entrance[1]] = "+" # mark as seen

        while queue:
            for _ in range(len(queue)):
                # process node
                cand_row, cand_col = queue.popleft()

                # check if it is at the border but not at entrance
                if [cand_row,cand_col] != entrance and (cand_row == 0 or cand_row == ROWS-1 or cand_col == 0 or cand_col == COLS-1):
                    return distance

                neighbs = [
                    (cand_row - 1, cand_col),
                    (cand_row + 1, cand_col),
                    (cand_row, cand_col - 1),
                    (cand_row, cand_col + 1)
                ]
                
                for neighb_row,neighb_col in neighbs:
                    # check if in bound, and is an empty cell and not visited already
                    if 0<=neighb_row<ROWS and 0<=neighb_col<COLS and maze[neighb_row][neighb_col] == ".":
                        maze[neighb_row][neighb_col] = "+" # mark as seen
                        queue.append((neighb_row,neighb_col)) # add to q
            distance += 1

        return -1

    