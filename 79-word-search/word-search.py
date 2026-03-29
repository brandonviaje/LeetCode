class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        we are given a board of letters and must search if a word exists
        we must return a boolean indicating if a word is present in this matrix

        idea: traverse each cell, perform a DFS and check if you can build the word
        if you cant, move onto the next cell until you reach the end of the cell
        """

        def DFS(row,col,index):
            # base case: if our index reaches out of bound we have found the word
            if index >= len(word):
                return True

            # prune: out of bounds/seen
            if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or board[row][col] == '.':
                return False

            # prune: char mismatch
            if board[row][col] != word[index]:
                return False

            # set as '.' to denote that we seen this
            board[row][col] = '.'

            # recurse further to check if we can find the word from here
            match = (DFS(row+1,col,index+1) or DFS(row-1,col,index+1) 
                        or DFS(row,col+1,index+1) or DFS(row,col-1,index+1))
           
            board[row][col] = word[index]  # undo/backtrack
            return match

        # iterate through the board
        for i in range(len(board)):
            for j in range(len(board[0])):
                # check if you can find the word from here
                if DFS(i,j,0):
                    return True

        return False
