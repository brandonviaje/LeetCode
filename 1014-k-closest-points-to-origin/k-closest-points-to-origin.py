class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        temp = [] # create temp list to convert to heap

        for x,y in points:
            # calculate distance for each point, find shortest distance
            distance = (x**2) + (y**2)
            temp.append([distance,x,y]) # add to list

        heapq.heapify(temp) # convert temp list to min heap

        result = []

        # pop k vals from min heap, KLOGN time
        while k > 0:
            distance,x,y = heapq.heappop(temp) 
            result.append([x,y])
            k -= 1

        return result

