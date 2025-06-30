# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        """
        do in order, to get sorted list, iterate through list to check
        """
        def inOrder(node):
            # base case
            if not node:
                return
            # L N R
            inOrder(node.left)
            sortTree.append(node.val)
            inOrder(node.right)

        sortTree = []
        inOrder(root)
        seen = {}

        # regular 2-sum problem
        for num in sortTree:
            diff = k - num

            if diff in seen:
                return True

            seen[num] = True

        return False
