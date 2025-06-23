# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []
            
        result = []
        queue = deque([root])

        while queue:

            level_size = len(queue)
            maxNum = float('-inf')

            # process level by level
            for _ in range(level_size):

                # process node
                cand = queue.popleft()
                if maxNum < cand.val:
                    maxNum = cand.val

                # add its children to queue
                if cand.left:
                    queue.append(cand.left)
                if cand.right:
                    queue.append(cand.right)

            result.append(maxNum) # add maxNum at that level

        return result