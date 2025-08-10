# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        queue = deque([(root)])
        result = []

        # BFS to build list
        while queue:
            lvl = []
            for i in range(len(queue)):
                # process node
                cand = queue.popleft()

                # stop at the very last
                lvl.append(cand.val)

                if cand.left:
                    queue.append(cand.left)
                if cand.right:
                    queue.append(cand.right)
            result.append(lvl)

        for i in range(len(result)):
            # if i is the last level, return the first element which is the very left
            if i == len(result)-1:
                return result[i][0]


        # T O(n^2) S O(n)