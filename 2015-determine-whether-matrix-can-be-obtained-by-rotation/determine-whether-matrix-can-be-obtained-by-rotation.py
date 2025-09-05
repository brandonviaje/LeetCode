class Solution(object):
    def findRotation(self, mat, target):
        """
        :type mat: List[List[int]]
        :type target: List[List[int]]
        :rtype: bool
        """

        # rotate the first matrix 90 degrees and check if they look the same as target matrix
        # perform a rotation 4 times, check if you ever get a matching pair
        for _ in range(4):
            top = 0
            bottom = len(mat) - 1

            # perform a vertical reversal
            while top < bottom:
                for col in range(len(mat)):
                    # perform the swap
                    mat[top][col],mat[bottom][col] = mat[bottom][col],mat[top][col]

                top += 1
                bottom -= 1

            # transpose the matrix
            for row in range(len(mat)):
                for col in range(row+1,len(mat)):
                    mat[row][col],mat[col][row] = mat[col][row],mat[row][col]

            # if the rotated matrix is the same as target return True
            if mat == target:
                return True

        # return false if no matches
        return False
        