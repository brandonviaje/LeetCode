# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        # if root is empty return 0
        if not root:
            return 0

        # contain root node and starting depth 1
        queue = deque([(root,1)])

        #BFS to find minimum depth
        while queue:

            cand, depth = queue.popleft()

            # if leaf node return depth
            if not cand.left and not cand.right:
                return depth
            
            if cand.left:
                queue.append((cand.left,depth+1))
            
            if cand.right:
                queue.append((cand.right,depth+1))
        
        