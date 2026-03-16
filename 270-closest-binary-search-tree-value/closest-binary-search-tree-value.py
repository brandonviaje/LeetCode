# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        self.closest = root.val

        # DFS
        def DFS(node):
            # base case 
            if not node:
                return

            curr_closest = abs(node.val - target)

            # check if current closest is < closest
            if curr_closest < abs(self.closest - target):
                self.closest = node.val
            if curr_closest == abs(self.closest - target):
                self.closest = min(self.closest, node.val)

            # traverse tree
            if node.val < target:
                DFS(node.right)
            else:
                DFS(node.left)

        DFS(root)
        return self.closest