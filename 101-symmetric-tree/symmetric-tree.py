# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def DFS(self,node1,node2):
        # if both empty return true
        if not node1 and not node2:
            return True

        # if one isnt empty return false
        if node1 and not node2 or not node1 and node2:
            return False

        # if val isnt equal return false
        if node1.val != node2.val:
            return False

        return self.DFS(node1.left,node2.right) and self.DFS(node1.right,node2.left)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # if empty its symmetric
        if  not root:
            return True

        # if there is a left and right check if its symmetric
        if root.left and root.right:
            return self.DFS(root.left,root.right)

        if not root.left and not root.right:
            return True
        
        # else that means either a left and no right or vice versa
        return False
    
        