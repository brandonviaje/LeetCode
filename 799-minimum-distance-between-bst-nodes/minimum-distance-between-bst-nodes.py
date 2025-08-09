# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        """
        intuition:

        the smallest numbers of a BST will always be on the left side of the tree, so we use in order trav
        to get 2 smallest and get the difference

        theres an edge case where if the smallest is 3 and 1 is 2 but lets say left side has 
        """


        def inOrder(root,result):
            if not root:
                return

            inOrder(root.left,result)
            result.append(root.val)
            inOrder(root.right,result)
        
        result = []
        inOrder(root,result)
        minDiff = float('inf')

        for i in range(len(result)):
            for j in range(i+1,len(result)):
                minDiff = min(minDiff, abs(result[i] - result[j]))

        return minDiff

        # T: O(n^2)
        # S: O(n)