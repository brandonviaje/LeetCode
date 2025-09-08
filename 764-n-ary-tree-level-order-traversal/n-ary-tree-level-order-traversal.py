"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """

        """
        do a BFS to get level order traversal
        """

        if not root:
            return

        def BFS(root):

            queue = deque([root])

            while queue:
                level_list = []
                curr_lvl = len(queue)
                # add to level list
                for _ in range(curr_lvl):
                    # process node and add it to list
                    node = queue.popleft()
                    level_list.append(node.val)

                    # process the children nodes now
                    for child in node.children:
                        queue.append((child))
                # add level list to result list
                result.append(level_list)

        result = []
        BFS(root)
        return result