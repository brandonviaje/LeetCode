# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:

        """
        BFS,
        9 + 15 = 24
        only take the left leaf when going down
        """

        queue = deque([root])
        total = 0
        
        while queue:
            cand = queue.popleft()

            # if theres a left leaf, update total and add to set to track that its a left node
            if cand.left:
                # check if the left node is a leaf node
                if not cand.left.left and not cand.left.right:
                    total += cand.left.val
                else:
                    queue.append(cand.left)

            if cand.right:
                queue.append(cand.right)

        return total


        