class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        """
        go through each cell, DFS adjacent cells add to ship count
        """

        ROWS = len(board)
        COLS = len(board[0])
        seen = set()
        ships = 0

        def DFS(row,col):
            stack = [(row,col)]
            seen.add((row,col))

            while stack:
                cand_row,cand_col = stack.pop()

                neighbs = [
                    (cand_row - 1, cand_col),
                    (cand_row, cand_col + 1),
                    (cand_row + 1, cand_col),
                    (cand_row, cand_col - 1)
                ]

                for neighb_row,neighb_col in neighbs:
                    # check for bounds,check if its already in seen, and also check if it is an X
                    if 0<= neighb_row < ROWS and 0<= neighb_col< COLS and (neighb_row,neighb_col) not in seen and board[neighb_row][neighb_col] == 'X':
                        seen.add((neighb_row,neighb_col))
                        stack.append((neighb_row,neighb_col))

        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == 'X' and (row,col) not in seen:
                    DFS(row,col)
                    ships += 1

        return ships