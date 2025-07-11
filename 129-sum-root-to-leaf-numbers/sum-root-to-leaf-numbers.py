# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        """
        some kind of pre order since you need the current node first
        you have to explore all paths and stop when there is a leaf node
        if root is none then return
        capture all root to leaf paths 
        """
        result = []
        def dfs(root,path):
            if not root:
                return

            # check for a leaf node
            if not root.left and not root.right:
                path.append(root.val)
                result.append([n for n in path])
                path.pop()
                return

            path.append(root.val)
            dfs(root.left, path) # explore left subtree
            dfs(root.right,path) # explore right subtree
            path.pop() # pop from path except root

        dfs(root,[])
        nums = []
        strN = ""
        
        for s in result:
            for num in s:
                strN =  strN + str(num)
            nums.append(int(strN)) # add to nums result
            strN = "" # reset string
        
        return sum(nums)