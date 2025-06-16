# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def dfs(self,root,result):
        if root is None:
            return

        result.append(root.val)

        # explore the left all the way
        if root.left:
            self.dfs(root.left,result)
        # explore the right all the way
        if root.right:
            self.dfs(root.right,result)

        return # backtracks and pops from call stack


    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.dfs(root,result)
        return result
        