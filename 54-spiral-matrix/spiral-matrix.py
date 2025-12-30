class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        size = len(matrix) * len(matrix[0])

        result = []
        
        left = 0
        right = len(matrix[0])
        top = 0
        bottom = len(matrix)
        
        while left < right and top < bottom:
            
            # left to right
            for i in range(left,right):
                result.append(matrix[top][i])

            top += 1

            # top to bottom
            for i in range(top,bottom):
                result.append(matrix[i][right -1 ])

            # check for valid subarray
            if len(result) == size:
                return result

            right -= 1
            # right to left
            for i in range(right-1,left-1,-1):
                result.append(matrix[bottom-1][i])
            
            bottom -= 1

            # bottom to top
            for i in range(bottom-1,top-1,-1):
                result.append(matrix[i][left])

            left += 1

        return result