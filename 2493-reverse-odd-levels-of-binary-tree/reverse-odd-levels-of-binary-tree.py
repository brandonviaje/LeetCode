# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        queue = deque([root])
        level = 0

        while queue:
            
            # if level is odd reverse the values at that node
            if level % 2 != 0:
                l,r = 0,len(queue)-1
                while l<=r:
                    queue[l].val,queue[r].val = queue[r].val,queue[l].val
                    l += 1
                    r -= 1
            
            for _ in range(len(queue)):
                cand = queue.popleft()
                
                if cand.left:
                    queue.append(cand.left)
                if cand.right:
                    queue.append(cand.right)

            level += 1

        return root