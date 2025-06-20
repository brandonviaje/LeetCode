# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def DFS(self,node: Optional[TreeNode],target, result, findSum, path):

        if node is None:
            return False
        
        # add node value to path
        path.append(node.val)
        # update sum
        findSum += node.val

        # check if its a leaf node
        if node.left is None and node.right is None:
            if(target == findSum):
                # add shallow copy of list
                result.append(list(path))

        # explore left side
        self.DFS(node.left,target,result,findSum,path)

        # explore the right side
        self.DFS(node.right,target,result,findSum,path)

        # backtrack
        path.pop()
                    

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []
        findSum = 0
        path = []
        self.DFS(root,targetSum, result, findSum, path)
        return result
        