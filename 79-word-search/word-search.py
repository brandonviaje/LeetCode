class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        backtrack
        """
        m, n = len(board), len(board[0])

        def backtrack(index, row, col):
            # base case
            if index >= len(word):
                return True
            if row < 0 or row >= m or col < 0 or col >= n:
                return False
            if board[row][col] == ".":
                return False
            if board[row][col] != word[index]:
                return False
            
            board[row][col] = "."

            # recurse to check if next char matches
            found = (backtrack(index+1,row + 1, col) or 
                    backtrack(index+ 1, row -1 , col) or 
                    backtrack(index+1,row,col+1) or 
                    backtrack(index+1,row,col-1))

            # undo/backtrack
            board[row][col] = word[index]
            return found

        for i in range(m):
            for j in range(n):
                # check if word is found
                if backtrack(0,i,j):
                    return True

        return False