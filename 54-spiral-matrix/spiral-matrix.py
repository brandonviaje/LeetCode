class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        [1,2,3]
        [4,5,6]
        [7,8,9]

        [1,2,3,4,5,6,7,8,9]

        [1,2,3,4]
        [5,6,7,8]
        [9,10,11,12]

        [1,2,3,4,8,12,11,10,9,5,6,7,8]

        - seen set to track the indexes we have already explored
        - order:
        start at top left to top right
        once we hit top right index: top right to bottom right
        once we hit bottom right index: bottom right to bottom left
        once we hit bottom lef index: bottom left to top left

        code for traversing each condition:
        for row in range(m):
            for col in range(n):
                if (row,col) == (0,n-1):
                    traverse down

                if (row,col) == (m-1,n-1):
                    traverse left
                
                if (row,col) == (m-1,0):
                    traverse up

                result.append(matrix[row][col])


        a big while loop that says while len(seen) < m*n
        - capture the first row
        - capture last elem of each row
        - capture

        optimal: use four pointers left,right,top,bottom to keep track and update the boundaries of the matrix
        - if left = right or top = bottom then we stop because we cant search anymore cells
        - after adding all values from top left right or bottom, update that specific pointer where appropriate
        """
        size = len(matrix) * len(matrix[0])
        result = []
        left,right = 0,len(matrix[0])
        top,bottom = 0,len(matrix)

        while left<right and top<bottom:
            
            # go from top left to top right
            for i in range(left,right):
                result.append(matrix[top][i])

            # update the top pointer since we finished scanning through that first top row
            top += 1

            # go from top right to bottom right now
            for i in range(top,bottom):
                result.append(matrix[i][right-1])

            # update the right pointer since we finished scanning through right column
            right -= 1

            # check if we have a valid submatrix after going through our first row and col
            if len(result) == size:
                break

            # go from bottom right to bottom left
            for i in range(right-1,left-1,-1):
                result.append(matrix[bottom-1][i])

            # update the bottom pointer since we finished scanning through entire bottom row
            bottom -= 1

            # go from bottom right to top left
            for i in range(bottom-1,top-1,-1):
                result.append(matrix[i][left])

            # update left pointer since we finished scanning through left column
            left += 1

        return result
     
        # T O(m*n) S O(n)