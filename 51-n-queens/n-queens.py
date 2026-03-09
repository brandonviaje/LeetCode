class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        posDiag = set() # row + col
        negDiag = set() # row - col

        # create result and board state
        result = []
        board = [['.'] * n for i in range(n)]

        # iterate through board row by row
        def backtrack(row):
            # base case, if reach end of board we found a distinct puzzle
            if row == n:
                result.append(["".join(row) for row in board]) # add board to result
                return
            
            # iterate through each col in row
            for col in range(n):
                # check if a queen occupies this diag/cols
                if col in cols or (row - col) in negDiag or (row+col) in posDiag:
                    continue
                
                cols.add(col)
                negDiag.add(row - col)
                posDiag.add(row + col)
                board[row][col] = "Q"

                backtrack(row+1) # recurse to next row

                # backtrack/undo
                cols.remove(col)
                negDiag.remove(row - col)
                posDiag.remove(row + col)
                board[row][col] = "."

        backtrack(0)
        return result