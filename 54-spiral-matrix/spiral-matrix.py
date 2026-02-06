class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        l,r = 0, len(matrix[0])
        t,b = 0, len(matrix)
        result = []

        while l < r and t < b:
            # top left to top right
            for i in range(l,r):
                result.append(matrix[t][i])
            
            t += 1
            # top right to bottom right
            for i in range(t,b):
                result.append(matrix[i][r-1])

            r -= 1

            # check if length of result is a sub matrix
            if len(result) == len(matrix)*len(matrix[0]):
                return result

            # bottom right to bottom left
            for i in range(r-1, l-1,-1):
                result.append(matrix[b-1][i])

            b -= 1

            # bottom left to top left
            for i in range(b-1,t-1,-1):
                result.append(matrix[i][l])

            l += 1

        return result
