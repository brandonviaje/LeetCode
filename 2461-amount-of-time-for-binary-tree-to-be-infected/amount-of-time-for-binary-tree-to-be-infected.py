# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        """
        convert tree to graph (DFS)
        run BFS starting from start node and keep track of how long it takes to cover whole tree
        """

        graph = defaultdict(list)

        stack = [root]

        while stack:
            node = stack.pop()
        
            if node.val == start:
                begin = node
            
            if node.right:
                graph[node].append(node.right)
                graph[node.right].append(node)
                stack.append(node.right)

            if node.left:
                graph[node].append(node.left)
                graph[node.left].append(node)
                stack.append(node.left)

        begin.val = 0
        queue = deque([begin])
        result = 0
        seen = set()

        # mark beginning node as seen
        seen.add(begin)

        while queue:
            cand_node = queue.popleft()
        
            # traverse neighbs
            for neighb in graph[cand_node]:
            
                if neighb not in seen:
                    queue.append(neighb)
                    neighb.val = cand_node.val + 1
                    result = max(result, neighb.val)

                seen.add(neighb)


        return result
