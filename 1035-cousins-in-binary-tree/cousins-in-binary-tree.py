# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:

    def DFS(self,node,target,depth):
        if not node:
            return

        if node.val == target:
            return depth
        
        # check left and right if needed
        return self.DFS(node.left, target, depth + 1) or self.DFS(node.right, target, depth + 1)
     

    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        queue = deque([root])
        children = {}

        # BFS to build children and parent relationship
        while queue:
            level = len(queue)
            for _ in range(level):
                cand = queue.popleft()
                if cand.left:
                    queue.append(cand.left)
                    children[cand.left.val] = cand # map left value to parent node
                if cand.right:
                    queue.append(cand.right)
                    children[cand.right.val] = cand # map right value to parent node

        # find depth of x and y
        left_depth =  self.DFS(root,x,0)
        right_depth = self.DFS(root,y,0)

        # return if cousin or not
        return(left_depth == right_depth) and children[x] != children[y]
        # T O(n) S O(n)