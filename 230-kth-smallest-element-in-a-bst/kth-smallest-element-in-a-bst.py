# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        in-order traversal to collect the ordered nodes

        after, that use a loop to decrement k until it hits 0, take that index and return it
        """

        def inOrder(root,result):
            # base case
            if not root:
                return 

            inOrder(root.left,result)
            result.append(root.val)
            inOrder(root.right,result)

        result = []
        inOrder(root,result) # in order traversal on a BST gives ordered list
        i = 0

        # scan through array until k is at 0, then we know we are at the i+1th index
        while k > 0:  
            k -= 1
            i += 1

        return result[i-1]