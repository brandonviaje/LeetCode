# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def isValid(self,node,low,high):
        if not node:
            return True

        # if the value is not in between low and high range 
        if not (low < node.val < high):
            return False 

        # validate left subtree with new upper bound and right subtree with new lower bound
        return self.isValid(node.left,low,node.val) and self.isValid(node.right,node.val,high)
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValid(root,float('-inf'),float('inf'))
        

    # T O(n) S O(h) : h is call stack height