class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        posDiag = set()
        negDiag = set()

        result = []
        board = [["."] * n for _ in range(n)]

        def backtrack(row):
            # base case
            if row == n:
                result.append(["".join(row) for row in board])
                return
            
            # iterate current col 
            for col in range(n):
                # skip current square if queen already on that col/diag
                if col in cols or (row-col) in negDiag or (row+col) in posDiag:
                    continue

                cols.add(col)
                negDiag.add(row-col)
                posDiag.add(row+col)
                board[row][col] = "Q"

                backtrack(row+1) # recurse further

                # undo/backtrack
                cols.remove(col)
                negDiag.remove(row-col)
                posDiag.remove(row+col)
                board[row][col] = "."

        backtrack(0)
        return result