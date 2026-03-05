class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        since we want to find what courses we need to take in order, we can use a topological sort approach.

        since the pair [0,1] indicates to take course 0, you must first take course 1, we see a dependency in here.

        we can iterate through each prereq, and do a directed relationship of the last elem and its first as an adj list

        once we create our adjacency list, we can do a topological sort on the graph
        """
        queue = deque()
        graph = defaultdict(list)
        in_degree = [0] * numCourses
        result = []

        # build adj list and update in_degree list
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            in_degree[course] += 1

        # check if a course doesn't need any prereqs
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)

        # BFS
        while queue:
            node = queue.popleft()
            result.append(node)

            # explore neighb courses that depend on current node
            for neighb in graph[node]:
                in_degree[neighb] -= 1 # reduce the prereq count of neighb since we already processed it

                # add unlocked courses to the queue
                if in_degree[neighb] == 0:
                    queue.append(neighb)

        return result if len(result) == numCourses else [] # return result if no cycle detected

        # T O(V+E)