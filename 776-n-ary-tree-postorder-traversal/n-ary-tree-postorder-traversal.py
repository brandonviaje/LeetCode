"""
# Definition for a Node.
class Node(object):
	def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        def DFS(root):

            if not root:
                return

            # recurse down first till u get to the very bottom
            for child in root.children:
                DFS(child)

            # add child to the result array
            result.append(root.val)

        result = []
        DFS(root)
        return result