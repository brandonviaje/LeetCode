class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """

        """
        instead of starting from every cell and seeing if water can reach the oceans,
        just start from the oceans and move inward.

        run DFS from all cells touching the Pacific and all cells touching the Atlantic.
        while moving inward, we’re only allowed to go to cells that are the same height
        or higher, since we’re basically going "uphill" in reverse.

        - anything the Pacific DFS can reach can flow to the Pacific.
        - anything the Atlantic DFS can reach can flow to the Atlantic.

        at the end, any cell that shows up in both visited sets is a cell that can send water to both oceans.
        """

        ROWS, COLS = len(heights), len(heights[0])
        pacific,atlantic = set(),set()
        result = []
        
        def dfs(r,c,ocean,prevHeight):
            # add to visited set
            ocean.add((r,c))
            stack = [(r,c)]

            while stack:
                cr,cc = stack.pop()
                # DFS on neighbors
                for nr,nc in [(cr+1,cc),(cr-1,cc),(cr,cc+1),(cr,cc-1)]:
                    # bounds check, check if already in visited set, and check if water can flow
                    if(0<=nr<ROWS and 0<=nc<COLS and (nr,nc) not in ocean and heights[nr][nc] >= heights[cr][cc]):
                        ocean.add((nr,nc))
                        stack.append((nr,nc))
        
        # O(n)
        for c in range(0,COLS):
            # build atlantic and pacific visited set
            dfs(0,c,pacific,heights[0][c])
            dfs(ROWS-1,c,atlantic,heights[ROWS-1][c])
        
        # O(n)
        for r in range(0,ROWS):
            # build atlantic and pacific visited set
            dfs(r,0,pacific,heights[r][COLS-1])
            dfs(r,COLS-1,atlantic,heights[r][COLS-1])

        #O(m*n)
        for i in range(ROWS):
            for j in range(COLS):
                if (i,j) in pacific and (i,j) in atlantic:
                    result.append((i,j))

        return result
        
        # O(n) + O(n) + O(m*n) = O(m*n)