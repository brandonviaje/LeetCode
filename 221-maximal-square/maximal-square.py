class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        """

        we want to figure out the biggest area.
        
        if we break it down into a subproblem, let (i,j) represent the top left of a square
        if we want to figure out if something is a square, we need to check the if the right,down and diagonally down right is a 1
        if it is, then that will be our first dimension. We want the minimum of that tho so we can have matching dimensions of the right bottom and bot right square

        T[i][j] = 0 : Return 0
        T[i][j] = 1 : Return 1 + min(T[i + 1][j], T[i][j + 1], T[i + 1][j+1])

        return max_size * max_size for the area

        """
        m = len(matrix)
        n = len(matrix[0])
        max_size = 0
        memo = {}
        def dp(row,col):
            if (row,col) in memo:
                return memo[(row,col)]

            if row >= m  or col >= n:
                return 0

            if matrix[row][col] == "0":
                return 0

            # check right, top, bottom right
            memo[(row,col)] = 1 + min(dp(row,col+1),dp(row+1,col),dp(row+1,col+1))
            return memo[(row,col)]

        for i in range(m):
            for j in range(n):
                # if we find a one, try to find max square size
                if matrix[i][j] == "1":
                    max_size = max(max_size,dp(i,j))

        return max_size * max_size