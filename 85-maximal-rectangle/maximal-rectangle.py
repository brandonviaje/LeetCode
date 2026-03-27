class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        """
        need to find max rectangle comprised of 1s in matrix
        brute force: traverse matrix and once you encounter a 1, try to compute the max rectangle

        optimized: we can capture the heights at each column, and then treat this problem like
        the largest rectangle in histogram problem using a monotonic stack
        """
        if not matrix or not matrix[0]:
            return 0

        ROWS,COLS = len(matrix), len(matrix[0])
        heights = [0] * (COLS+1)
        max_area = 0

        for row in matrix:
            for i in range(COLS):
                # get heights for each column
                if row[i] == '1':
                    heights[i] = heights[i] + 1
                else:
                    heights[i] = 0
            
            stack = [-1]

            # solve area of rectangle using stack after updating heights arr
            for i in range(COLS+1):
                while stack and heights[i] < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    w = i - stack[-1] - 1
                    max_area = max(max_area, h * w)
                stack.append(i)

        return max_area