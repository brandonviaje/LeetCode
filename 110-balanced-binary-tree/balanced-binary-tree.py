# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        
        """
        post order traversal so that you can know the depth 
        and then basically you can just compare by subtracting the left and right depths 
        and checking if they dont differ no more than 1
        """

        if not root:
            return True

        def DFS(root):
            # return 0 if u come across an empty node
            if not root:
                return 0

            left = DFS(root.left)
            # return -1 up the tree if we found an imbalance already
            if left == -1:
                return -1
            right = DFS(root.right) 
            # return -1 up the tree if we found an imbalance already
            if right == -1:
                return -1

            # check if the depths are greater than 1, if it isnt then its not balanced
            if abs(left-right) > 1:
                return -1

            # return the depth
            return 1 + max(left,right)

        return DFS(root) != -1
        