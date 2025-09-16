"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """


        """
        intuition:

        - do a BFS and build the result list, just return the length of it after so that you can get the max levels
        """

        if not root:
            return 0

        res = []
        queue = deque([root])

        while queue:
            level_list = []
            for _ in range(len(queue)):
                # pop the cand value and then get its children to further process, build the level list
                cand_val = queue.popleft()

                # traverse through the children nodes
                for node in cand_val.children:
                    level_list.append(node.val)
                    queue.append(node)

            # add this to the result list
            res.append(level_list)
        
        return len(res)
        
        # T O(n) S O(n)