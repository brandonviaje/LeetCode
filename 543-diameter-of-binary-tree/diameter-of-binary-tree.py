# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        create a result variable to store the longest diameter

        result = 0
        """

        self.result = 0

        def dfs(root):
            # base case
            if root is None:
                return 0

            # post order
            left = dfs(root.left)
            right = dfs(root.right)

            self.result = max(self.result, left + right)

            # return the longest depth and add 1 to account for current lvl
            return max(left,right) + 1

        dfs(root)
        return self.result