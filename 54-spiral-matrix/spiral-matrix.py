class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        l,r = 0, len(matrix[0])
        t,b = 0, len(matrix)

        M,N = len(matrix),len(matrix[0])
        result = []

        while l < r and t < b:
            
            # add top left to top right
            for i in range(l,r):
                result.append(matrix[t][i])
            
            t += 1

            # add top right to bottom right
            for j in range(t, b):
                result.append(matrix[j][r-1])

            r -= 1

            # check if matrix is square
            if len(result) == M * N:
                return result

            # add bottom right to bottom left
            for i in range(r-1,l-1,-1):
                result.append(matrix[b-1][i])

            b -= 1

            # add bottom left to top left
            for j in range(b - 1, t-1, -1):
                result.append(matrix[j][l])
            l += 1

        return result