"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        

        """
        run a DFS on the root, and then add it to the result array

        after that, you can recursively visit its children so that you can get a preorder traversal
        """

        def DFS(root):
            # base case
            if not root:
                return

            result.append(root.val)
            
            # recurse down the tree 
            for node in root.children:
                DFS(node)

        result = []
        DFS(root)
        return result

        # T O(N) S O(N) where N is the number of nodes in the tree