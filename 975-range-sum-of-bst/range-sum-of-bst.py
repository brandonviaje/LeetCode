# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: Optional[TreeNode]
        :type low: int
        :type high: int
        :rtype: int
        """
        
        """
        run a dfs, and keep track of a global result variable
        check if the node is currently in that range of low and high

        if the node is in that range, add the nodes value to the global result variable
        """
        self.result = 0

        def dfs(node):
            if not node:
                return 

            # check if the node value is in the range of low and high
            if low<=node.val<=high:
                self.result += node.val

            # traverse the subtree
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return self.result

    # T: O(n)