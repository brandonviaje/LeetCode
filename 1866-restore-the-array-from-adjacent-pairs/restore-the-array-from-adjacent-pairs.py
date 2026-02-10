class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        """
        every pair of adjacent elements , what we can do is treat this as a graph
        and so that we know what nodes we visited already, and then we just travverse to the neighbor that is not in prev
        """

        # build adj list
        graph = defaultdict(set)

        for u,v in adjacentPairs:
            graph[u].add(v)
            graph[v].add(u)

        start = None

        # check for a starting node that has only one neighbor
        for node, neighbs in graph.items():
            if len(neighbs) == 1:
                start = node
                break

        result = [start]

        # run a DFS , iterate through adjacency list of starting node
        while graph[start]:
            node = graph[start].pop()   # take neighb
            result.append(node)         # add to result
            graph[node].remove(start)   # remove neighb and curr node connection
            start = node                # set curr node to neighb node 

        return result