# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """
        self.dfs(root.left,result)
        """
        result = 0
        return self.dfs(root, result, targetSum)

    def dfs(self, root, result, targetSum): # inorder traversal, go as far left, then check right, backtrack
        if root is None:
            return False
        # [5, 4, 11, 2]
        result += root.val

        if not root.right and not root.left: # if a leaf node
            print(f"{root.val} is a leaf, current result is {result} target is {targetSum}")
            return result == targetSum

        return self.dfs(root.left, result, targetSum) or self.dfs(root.right, result, targetSum)
        
        

            
        