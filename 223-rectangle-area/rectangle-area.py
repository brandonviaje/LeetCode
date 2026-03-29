class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        """
        (ax1,ay1): bottom left
        (ax2,ay2): top right

        (bx1, by1): bottom left
        (bx2, by2): top right
        """

        h_1,w_1 = ax2 - ax1, ay2 - ay1
        h_2,w_2 = bx2 - bx1, by2 - by1
        area_1 = h_1 * w_1
        area_2 = h_2 * w_2

        # calculate x and y overlap
        x_overlap = min(ax2,bx2) - max(ax1,bx1)
        y_overlap = min(ay2,by2) - max(ay1,by1)

        # check if they overlap
        if x_overlap > 0 and y_overlap > 0:
            intersection = x_overlap * y_overlap
            return (area_1+area_2) - intersection
   
        return area_1 + area_2

        # T O(1) S O(1)