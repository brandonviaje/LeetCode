# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []

        queue = deque([root])
        result = []

        while len(queue) > 0:

            level_list = []

            # loop through entire level
            for _ in range(len(queue)):

                cand = queue.popleft()
                level_list.append(cand.val)

                # check if it has children and add to q
                if cand.left:
                    queue.append(cand.left)
                if cand.right:
                    queue.append(cand.right)
            
            result.append(level_list)

        return result

        # T O(n) S O(n)