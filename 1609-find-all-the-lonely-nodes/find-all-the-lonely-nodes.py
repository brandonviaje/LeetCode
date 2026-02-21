# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        """
        post order traversal, so you can start bottom up and check if you have any siblings

        then check
        """
        self.result = []

        # dfs to traverse the tree
        def dfs(node):
            # base case: check if lonely node
            if node.left and not node.right:
                self.result.append(node.left.val)
            if node.right and not node.left:
                self.result.append(node.right.val)

            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)

        dfs(root)
        return self.result