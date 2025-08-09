# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        i = 0
        result = -1

        def dfs(root):
            nonlocal i
            nonlocal result
            if not root:
                return

            dfs(root.left)

            i += 1

            # if i is equal to k, we found our kth smallest since we are doing in order
            if i == k:
                result = root.val
                return

            dfs(root.right)

        dfs(root)
        return result
        