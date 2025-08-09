# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        basically , if the descendants of a spefici node doesnt have a 1, prune it
        - you need to do post order i believe, so that you know which subtrees dont contain a 1, so that you can prune it
        - DFS to do this

        - check if it has a 1 by doing a DFS, a flag to mark true if it is and then return, 
        - to get rid of a subtree, set that said pointer to Null
        """

        """
        when checking for all 0s do a post order traversal, as soon as you see 1, return True all the way up

        """
        head = root

        # DFS to check if it contains a 1
        def DFS(root):
            if not root:
                return False

            if root.val == 1:
                return True

            left = DFS(root.left)
            right = DFS(root.right)

            return (left or right)

        # check if current val is a 0

        # check if left and right subtree has a 1
        checkSelf = DFS(root)
        checkLeft = DFS(root.left)
        checkRight = DFS(root.right)


        # prune if the subtree has no 1 in it
        if not checkSelf:
            return None

        if not checkLeft:
            root.left = None
        
        if not checkRight:
            root.right = None

        # after that we recurse further

        if root.left:
            self.pruneTree(root.left)

        if root.right:
            self.pruneTree(root.right)

        return head