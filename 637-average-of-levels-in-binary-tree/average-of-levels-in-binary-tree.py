# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        if not root:
            return []

        queue = deque([root])
        result = []

        while queue:

            # save queue size
            level_nodes = len(queue)
            average = 0

            # for each node in the current level
            for _ in range(level_nodes):
                cand = queue.popleft()
                average += cand.val

                if cand.left:
                    queue.append(cand.left)
                if cand.right:
                    queue.append(cand.right)

            # divide average by how many nodes there were
            average /= level_nodes
            result.append(average)

        return result

        # T O(n) S O(m) : m is max num of nodes in the tree
        