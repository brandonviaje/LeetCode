# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        queue = deque([root])
        result = []


        # perform BFS and collect nodes at each level
        while queue:
            
            level_list = []
            for _ in range(len(queue)):
                cand = queue.popleft()
                level_list.append(cand.val)
                if cand.left:
                    queue.append(cand.left)
                if cand.right:
                    queue.append(cand.right)

            result.append(level_list)

        # reverse list after
        return result[::-1]