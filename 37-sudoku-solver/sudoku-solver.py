class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """Do not return anything, modify board in-place instead."""
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        nums = ['1','2','3','4','5','6','7','8','9']
                
        def backtrack(index):
            """
            If all possible values cannot go into current cell, backtrack
            This means each value we try, is either already in the row, col, or grid of this cell
            """
            
            # backtrack with pruning to make it more efficient 
            # backtrack boilerplate
            
            # 1. base case
            if index == len(coords):
                return True
                
            row, col = coords[index]
            boxI = (row//3) * 3 + (col//3)

            # 2. try a decision
            for num in nums:
                # pruning part
                if num not in rows[row] and num not in cols[col] and num not in boxes[boxI]:
                    # modify in place
                    # add to the set at that row col and box index
                    board[row][col] = num
                    rows[row].add(num)
                    cols[col].add(num)
                    boxes[boxI].add(num)
                    
                    # 3. recurse to explore the board
                    if backtrack(index + 1):
                        return True
                        
                    # 4. backtrack/undo
                    board[row][col] = "."
                    rows[row].remove(num)
                    cols[col].remove(num)
                    boxes[boxI].remove(num)
                
            return False
            
        # must track the numbers already on the grid
        coords = []
        
        for i in range(9):
            for j in range(9):
                # if empty conntinue
                if board[i][j] == ".":
                    coords.append((i,j))
                else: #else add number to set for its row, col, and box
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    boxes[(i//3) * 3 + (j//3)].add(board[i][j])
        
        backtrack(0)