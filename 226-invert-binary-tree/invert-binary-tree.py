# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root:
            return 

        # invert subtrees
        l = self.invertTree(root.left)
        r = self.invertTree(root.right)


        # swap left and right
        root.left = r
        root.right = l

        return root
        