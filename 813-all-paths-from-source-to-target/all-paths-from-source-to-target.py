class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        """
        have to find number of paths from source to target.
        one way we can do that is through DFS.

        process current node and path so far
        explore next connected nodes of the current node, and build the path by adding that next node
        """

        target = len(graph) - 1
        result = []
        stack = [(0, [0])]                              # stack (current_node, path)

        while stack:
            node, path = stack.pop()                    # pop current node, current path so far

            # check if we reach leaf node (end of graph)
            if node == target:
                result.append(path)                     # add path to result
                continue    

            # traverse through connected neighbs of current node
            for neighb in graph[node]:
                stack.append((neighb, path + [neighb]))  # add neighb to stack and build path

        return result