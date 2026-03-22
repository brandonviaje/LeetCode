class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        m, n = len(matrix), len(matrix[0])
        first_col = False
        first_row = False

        # check if first row and col has 0
        for row in range(m):
            if matrix[row][0] == 0:
                first_col = True
                break

        for col in range(n):
            if matrix[0][col] == 0:
                first_row = True
                break

        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 0:
                    # mark first col and row as zero
                    matrix[row][0] = 0
                    matrix[0][col] = 0

        for row in range(1,m):
            for col in range(1,n):
                if matrix[row][0] == 0 or matrix[0][col] == 0:
                    # mark as zero
                    matrix[row][col] = 0

        # pad first rows and cols with zeroes
        if first_col:
            for i in range(m):
                matrix[i][0] = 0

        if first_row:
            for j in range(n):
                matrix[0][j] = 0

                

                