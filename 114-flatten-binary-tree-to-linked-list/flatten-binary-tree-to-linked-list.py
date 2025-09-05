# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root: return
        treeList = []

        def DFS(root):
            if not root:
                return
            # add the root to the list
            treeList.append(root)
            DFS(root.left)
            DFS(root.right)

        # add it to the list
        DFS(root)
        # assign the nodes left pointer to null and the point to the next 
        for i in range(len(treeList)-1):
            treeList[i].left = None
            treeList[i].right = treeList[i + 1]