class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        """
        build graph/adj list

        then, do a DFS from source that checks if we can reach the destination

        if we end up at the destination during DFS, return True
        return False after DFS
        """
        graph = defaultdict(list)
        seen = set()

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # DFS from src node to check if we end up at dest
        stack = [source]

        while stack:
            node = stack.pop()

            # check if curr node is destination
            if node == destination:
                return True
            
            # go through adj list
            for neighb in graph[node]:
                # skip if already seen
                if neighb in seen:
                    continue

                # add to stack and set
                stack.append(neighb)
                seen.add(neighb)
                

        return False