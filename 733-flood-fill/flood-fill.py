from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        """
        BFS, to change the color avoid any cells with a 0, and we must start on sr and sc
        """

        # return early to prevent infinite loop
        if image[sr][sc] == color:
            return image 

        queue = deque([(sr,sc)])

        # capture starting pixel
        pixel = image[sr][sc]
        print("pixel:",pixel)

        # set to color after
        image[sr][sc] = color
        print(image)

        # BFS to explore all adjacents path 
        while queue:

            # process curent node
            cand_row,cand_col = queue.popleft()

            # get neighbs of it and loop through it to check if its the og pixel color
            neighbs = [
                (cand_row - 1,cand_col),
                (cand_row,cand_col + 1),
                (cand_row + 1,cand_col),
                (cand_row,cand_col - 1)
            ]

            for neighb_row, neighb_col in neighbs:
                # error bounds, check if = to pixel color
                if 0<=neighb_row<len(image) and 0<=neighb_col<len(image[0]) and image[neighb_row][neighb_col] == pixel:
                    image[neighb_row][neighb_col] = color
                    queue.append((neighb_row,neighb_col))

        return image
