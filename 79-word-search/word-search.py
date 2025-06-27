class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])

        # DFS every cell check if it equals to word at index
        def dfs(row,col,index):
            # base case
            if index == len(word):
                return True 
            # check if out of bounds, marked as visited, or if equals to word at index
            if (row < 0 or col < 0 or row >= ROWS or col >= COLS or board[row][col] == '.' or board[row][col] != word[index]):
                return False

            # mark in place as visited
            board[row][col] = '.'

            # explore all neighbours of cell check if it equals word at next index
            result = (dfs(row-1, col,index+1) or
                      dfs(row, col+1,index+1) or
                      dfs(row+1, col,index+1) or
                      dfs(row, col-1,index+1))   

            board[row][col] = word[index] # switch back after exploring

            return result

        for row in range(ROWS):
            for col in range(COLS):
                if dfs(row,col,0): 
                    return True

        return False

        """
        - bruteforce the combinations
        - DFS every cell
        - base case if index same as len of word
        [A,B,C,E]
        [S,F,C,S]
        [A,D,E,E] checks each cell if it starts with our first letter
        """