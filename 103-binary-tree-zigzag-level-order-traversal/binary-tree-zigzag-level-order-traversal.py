# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        queue = deque([root])
        result = []
        flip = 0

        while queue:

            level_list = []
            
            for _ in range(len(queue)):
                cand = queue.popleft()
                level_list.append(cand.val)

                if cand.left:
                    queue.append(cand.left)
                if cand.right:
                    queue.append(cand.right)
                    
            # if its time to flip, reverse the level list
            if flip == 1:
                level_list.reverse()

            result.append(level_list)
            flip = flip ^ 1 # flip sign

        
        return result

        # T O(n) S O(n)