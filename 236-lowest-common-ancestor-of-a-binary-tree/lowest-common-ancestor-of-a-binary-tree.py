# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # base  case if you found the nodes or empty
        if not root or root == p or root == q:
            return root

        # explore left subtree and right subtree for the nodes
        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q)
        
        # if you were able to find both left and right, this root is the LCA
        if left and right:
            return root

        return left if left else right