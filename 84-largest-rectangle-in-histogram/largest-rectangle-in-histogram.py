class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        [2,1,5,6,2,3]     

        # brute force: try every possible combo
        result = float('-inf')
            
        for i in range(len(heights)):
            min_height = heights[i]
            for j in range(i, len(heights)):
                min_height = min(min_height, heights[j])
                width = j - i + 1
                result = max(result, min_height * width)

        return result
        """

        stack = [-1]
        max_area = 0

        for i in range(len(heights)):
            # resolve bars taller than current
            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                max_area = max(max_area, h * w)

            stack.append(i)

        # resolve remaining bars (right boundary = end)
        while stack[-1] != -1:
            h = heights[stack.pop()]
            w = len(heights) - stack[-1] - 1
            max_area = max(max_area, h * w)

        return max_area