class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        """
        every house can be warmed

        return minimum radius standard of heaters s.t. those heater warm all houses
        """
        heaters.sort()
        radius = float('-inf')
        
        for house in houses:
            l,r = 0, len(heaters)-1
            dist = float('inf')

            # binary search to get min distance of curr house
            while l<r:
                mid = (l+r)//2
                if heaters[mid] < house:
                    l = mid + 1
                else:
                    r = mid

            dist = min(dist, abs(heaters[l] - house))

            if l > 0:
                dist = min(dist, abs(heaters[l-1] - house))

            radius = max(radius, dist)

        return radius