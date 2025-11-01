# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def rob(self, root: Optional[TreeNode]) -> int:

        memo = {}
        """

        SUBPROBLEM: either take from the current level, or skip and take from the next levels.
        get the max out of those problems.

        T(n) = O(n)

        """

        def DFS(node):
            # if already computed
            if node in memo:
                return memo[node]

            # base case
            if not node:
                return 0
            
            # case 1: take current node skip its children
            caseOne = node.val
            
            if node.left:
                caseOne += DFS(node.left.left) + DFS(node.left.right)
            if node.right:
                caseOne += DFS(node.right.left) + DFS(node.right.right)

            # case 2: skip current node, and take its children
            caseTwo = DFS(node.left) + DFS(node.right)

            # get max value out of both cases
            memo[node] = max(caseOne,caseTwo)
            return memo[node]

        return DFS(root)