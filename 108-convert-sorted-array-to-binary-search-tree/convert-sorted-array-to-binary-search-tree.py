# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        """
        in-order traversal is what converts a tree to a sorted list
        build the tree from the bottom up
        so post order traversal is needed
        """

        # base case
        if not nums:
            return

        # get root
        mid = len(nums) // 2
        root = TreeNode(nums[mid])

        # build left and right subtrees recursively
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1:])
        
        return root