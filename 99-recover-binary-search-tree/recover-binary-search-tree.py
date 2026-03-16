# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        valid BST: left subtree < curr and right subtree > curr

        - since its a BST(not valid yet) an in-order traversal gives you a sorted arr
        - since exactly two nodes were swapped, then we get an almost sorted array
        - iterate through arr, if we find left val < right val then we found the values that must be swapped
        - do a DFS and if curr val == x, update its val, if curr val == y, update its val
        """
        self.arr = []
        stack = [root]

        def inOrder(root):
            # base case
            if not root:
                return

            inOrder(root.left)
            self.arr.append(root.val)
            inOrder(root.right)

        inOrder(root) # build arr

        # iterate through arr, check what values have been swapped/not sorted
        x = y = None

        for i in range(len(self.arr)-1):

            # check if out of order
            if self.arr[i] > self.arr[i+1]:
                y = self.arr[i+1]
                
                if x is None:
                    x = self.arr[i]
                else:
                    break

        # go back into tree, and if you see the values swap it with the other
        while stack:
            node = stack.pop()

            if node:
                # swap values
                if node.val == x:
                    node.val = y    
                elif node.val == y:
                    node.val = x

                # add left and right subtree to stack
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)