# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        parent = {}
        stack = [root]

        # DFS 
        while stack:
            node = stack.pop()

            # check if it is starting node
            if node.val == start:
                begin =  node

            if node.right:
                parent[node.right] = node
                stack.append(node.right)

            if node.left:
                parent[node.left] = node
                stack.append(node.left)

        queue = deque([(begin,0)]) # (node, 0)
        seen = {begin}             # mark start node as seen
        result = 0

        while queue:
            node, time = queue.popleft()
            result = max(result,time)    

            # check curr nodes children and parent (if it exists)
            for neighb in (node.left, node.right, parent.get(node)):
                if neighb and neighb not in seen:
                    seen.add(neighb)
                    queue.append((neighb,time+1))

        return result