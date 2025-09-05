class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        

        """
        since they want us to do it in-place, we must have to use two pointers coding pattern

        trivial approach: create a matrix and fill it in according to the post transformation

        the way we can do it is have 4 pointers allocated for each side: up,r,l,down and then update the pointers 
        based on some logic.. We cant allocate another matrix so the memory complexity will be O(1)

        regarding time complexitys it would be O(n^2)

        what i notice is if you take the first row and write it from left to right and from top to bottom itll show a rotation

        how to rotate a matrix 90 degrees:
        - perform a vertical reverse
        - transpose the matrix, to transpose just swap the matrix at [row][col] with [col][row]
        """

        matrixSize = len(matrix)

        top = 0

        bottom = matrixSize - 1

        # perform a vertical reverse 
        while top < bottom:
            for col in range(matrixSize):
                # perform the swap
                matrix[top][col],matrix[bottom][col] = matrix[bottom][col],matrix[top][col]

            # update pointer
            top += 1
            bottom -= 1

        # transpose the matrix 
        for row in range(matrixSize):
            for col in range(row + 1, matrixSize):
                # perform transposition
                matrix[row][col], matrix[col][row] = matrix[col][row],matrix[row][col]

        return matrix

        # T O(n^2) S O(1)