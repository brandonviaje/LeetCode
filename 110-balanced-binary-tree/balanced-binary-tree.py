# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(root):
            # base case 
            if not root:
                return 0

            # recurse through our subtree
            left = dfs(root.left)
            right = dfs(root.right)

            # check if height balanced
            if abs(left - right) > 1:
                return float('-inf')

            return 1 + max(left,right)

        return True if dfs(root) != float('-inf') else False