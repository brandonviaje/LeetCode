# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        """
        merge the node: if two nodes overlap, add them together

        check if both trees have a left and right
        """
        if not root1 and not root2: 
            return None

        # merge the node: if two nodes overlap, add them together
        result = TreeNode((root1.val if root1 else 0) + (root2.val if root2 else 0))

        # check if both trees have a left and right, add to it if there is
        result.left = self.mergeTrees(root1 and root1.left, root2 and root2.left)
        result.right = self.mergeTrees(root1 and root1.right, root2 and root2.right)

        return result


