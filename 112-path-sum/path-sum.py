# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def DFS(self, node:Optional[TreeNode], targetSum:int, findSum:int):
        if node is None:
            return False

        # update sum
        findSum += node.val

        # check if it's a leaf
        if node.left is None and node.right is None:
            return targetSum == findSum
        
        # else explore left tree or right tree if available until we get a leaf node
        return self.DFS(node.left,targetSum, findSum) or  self.DFS(node.right,targetSum, findSum)

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        findSum = 0
        # call DFS
        return self.DFS(root,targetSum,findSum)
        