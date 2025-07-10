# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        """
        map current node val to the parent node using BFS and a  hashmap
        identify the depths of the node and check if the left depth == right depth and parent[left.val] != parent[right.val]!= 0
        """

        def dfs(root,target,depth):
            # base case
            if not root:
                return  
            # if found return depth
            if root.val == target:
                return depth
            # explore left or right subtrees for val
            return dfs(root.left,target,depth + 1) or dfs(root.right,target,depth+1)

        queue = deque([root])
        parent = {}

        while queue:
            
            cand = queue.popleft()

            # map values to corresponding parent node
            if cand.left:
                parent[cand.left.val] = cand
                queue.append(cand.left)
            if cand.right:
                parent[cand.right.val] = cand
                queue.append(cand.right)

        # DFS until you hit the target nodes, get depth from it
        x_depth = dfs(root,x,0)
        y_depth = dfs(root,y,0)

        # return if its a parent
        return x_depth == y_depth and parent[x] != parent[y]