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
        leftNode = set()
        
        while queue:
            cand = queue.popleft()

            # check if its in the set and is a leaf node
            if not cand.left and not cand.right and cand in leftNode:
                total += cand.val

            # if theres a left leaf, update total and add to set to track that its a left node
            if cand.left:
                leftNode.add(cand.left)
                queue.append(cand.left)

            if cand.right:
                queue.append(cand.right)

        return total


        