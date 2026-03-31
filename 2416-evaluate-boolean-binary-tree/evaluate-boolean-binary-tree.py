# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        """
        0 - False
        1 - True
        2 - OR
        3 - AND

        evaluate expression
        """

        def dfs(node):
            if not node:
                return

            if node.val == 0:
                return False

            if node.val == 1:
                return True

            if node.val == 2:
                left = dfs(node.left)
                right = dfs(node.right)
                return left or right
            if node.val == 3:
                left = dfs(node.left)
                right = dfs(node.right)
                return left and right
                
        return dfs(root)