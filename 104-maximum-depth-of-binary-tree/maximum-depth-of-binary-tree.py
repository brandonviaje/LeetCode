# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        # traverse left n right subtree
        left_tree = self.maxDepth(root.left)
        right_tree = self.maxDepth(root.right)

        # take max depth out of both subtrees
        maxDepth = max(left_tree,right_tree)

        # return maxDepth add 1 for the current level
        return 1 + maxDepth