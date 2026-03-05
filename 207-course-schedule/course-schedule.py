class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        we can do a BFS topological sort here, because if we find that the numCourses = len(result), then we can complete 
        all courses else we cant
        """

        result = 0
        graph = defaultdict(list)
        in_degree = [0] * numCourses

        # build adjacency list and in degree array
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            in_degree[course] += 1

        queue = deque()
        # process courses that don't have a prerequisite
        for i in range(numCourses): 
            if in_degree[i] == 0:
                queue.append(i)

        # BFS topological sort
        while queue:
            node = queue.popleft()
            result += 1

            # check neighbors of current course
            for neighb in graph[node]:
                in_degree[neighb] -= 1

                # add to queue if there's no prerequisites
                if in_degree[neighb] == 0:
                    queue.append(neighb)

        return result == numCourses
