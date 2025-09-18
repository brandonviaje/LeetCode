class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """

        """
        intuition:
        - we need to check if we can visit all of the rooms
        - DFS can help us explore room 0 all the way down
        -we access the room and grab the key
        - we then follow that room where the key is

        how can we keep track of everything visited?
        - we can create a set and compare the two as our return boolean statement
        - we create another set to store our rooms that we have visited
        - after adding it ot the set we explore that keys room index
        """

        n = len(rooms)
        seen = [False] * n
        seen[0] = True
        stack = [0]

        # DFS on each room
        while stack:
            u = stack.pop()
            for v in rooms[u]:
                # if not in seen yet, mark as seen and add to stack
                if not seen[v]:
                    seen[v] = True
                    stack.append(v)

        # return to check if everything in seen is true or empty
        return all(seen)

        # T O(n) S O(n)