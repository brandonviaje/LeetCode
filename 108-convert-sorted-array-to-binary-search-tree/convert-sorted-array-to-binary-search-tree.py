# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def DFS(l,r):
            # base case
            if l > r:
                return

            mid = (l + r) // 2         # take middle
            root = TreeNode(nums[mid]) # set root node

            # build left and right sutbree
            root.left = DFS(l,mid-1)
            root.right = DFS(mid+1,r)

            return root

        return DFS(0,len(nums)-1)