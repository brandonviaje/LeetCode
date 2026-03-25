class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        max_area = float('-inf')
        longest_diagonal = 0

        # grab longest diagonal
        for l,w in dimensions:
            if longest_diagonal <= sqrt((l*l) + (w*w)):
                longest_diagonal = sqrt((l*l) + (w*w))

        # if multiple rectangles have longest diagonal, then get max_area of it
        for l,w in dimensions:
            if longest_diagonal == sqrt((l*l) + (w*w)):
                max_area = max(max_area, l*w)

        return max_area