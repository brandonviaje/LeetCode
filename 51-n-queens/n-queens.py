class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        posDiag = set() # r + c
        negDiag = set() # r - c

        # create board state and result list
        result = []
        board = [["."] * n for i in range(n)]

        # iterate row by row
        def backtrack(row):
            # base case:if we reached end of board add to result
            if row == n:
                result.append(["".join(board[r]) for r in range(n)])
                return

            # try every col in the row
            for col in range(n):
                # skip if prev queen is placed on same col/diags
                if col in cols or (row+col) in posDiag or (row-col) in negDiag:
                    continue

                # add to set/update board
                cols.add(col)
                posDiag.add(col+row)
                negDiag.add(row-col)
                board[row][col] = "Q"

                backtrack(row+1) # recurse further

                # undo
                cols.remove(col)
                posDiag.remove(col+row)
                negDiag.remove(row-col)
                board[row][col] = "." 

        backtrack(0)
        return result
        