class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.

        you can do a multi-source BFS, keep track of where all the gates are, add them to a queue
        then, do a BFS on each of the gates to get the shortest path of each.

        if there is a path that is smaller than the current, then overwrite it.
        """
        if not rooms:
            return

        queue = deque()
        ROWS,COLS = len(rooms), len(rooms[0])

        # iterate through grid and capture where all the gates are
        for row in range(ROWS):
            for col in range(COLS):
                if rooms[row][col] == 0:
                    queue.append((row,col))

        # BFS USING GATES
        while queue:
            cand_row,cand_col = queue.popleft()

            neighbs = [(cand_row+1,cand_col), (cand_row-1,cand_col),(cand_row,cand_col+1),(cand_row,cand_col-1)]
            
            # check curr gates neighbors
            for nr,nc in neighbs:
                # bounds check, avoid walls
                if 0<= nr < ROWS and 0<= nc < COLS and  rooms[nr][nc] == 2147483647:
                    rooms[nr][nc] = rooms[cand_row][cand_col] + 1 # add 1 from prev
                    queue.append((nr,nc))
                        