# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        """
        basically do a DFS on every path
        """

        if not root:
            return 0

        def dfs(root,nodes):
            paths = 0

            # if found targetsum increment paths
            if nodes == targetSum:
                paths += 1

            # explore possible paths on left and right subtree
            if root.left:
                paths += dfs(root.left, nodes + root.left.val)
            if root.right:
                paths += dfs(root.right, nodes + root.right.val)

            return paths

        return(dfs(root,root.val) + self.pathSum(root.left,targetSum) + self.pathSum(root.right,targetSum))