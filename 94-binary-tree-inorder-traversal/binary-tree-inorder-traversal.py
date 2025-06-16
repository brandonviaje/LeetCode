# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def dfs(self, root: Optional[ListNode], result):
        # base case
        if root is None:
            return

        if root.left:
            self.dfs(root.left,result)

        result.append(root.val)
        
        if root.right:
            self.dfs(root.right,result)

        return
        

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        result = []
        self.dfs(root,result)
        return result
        