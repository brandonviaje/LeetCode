class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        """
        two pointers

        alice: left to right
        bob: right to left

        return num of times alice and bob have to refill to water all plants
        intuition: subtract from capacity then we have to do a  check if its < the current plant they're on
        if it is, then increment refills and set capacityA back to starting same thing for capcityB

        [1,2,4,4,5]
             ^
             ^
        alice = 3
        bob = 5
        refill = 1
        """
        # capture the initial capacity
        alice = capacityA
        bob = capacityB
        refill = 0

        l,r = 0,len(plants)-1

        while l < r:
            # refill if alice cant water current plant
            if capacityA < plants[l]:
                refill += 1
                capacityA = alice

            # refill if bob cant water current plant
            if capacityB < plants[r]:
                refill += 1
                capacityB = bob
            
            # update capacity and pointers
            capacityA -= plants[l]
            capacityB -= plants[r]
            
            l += 1
            r -= 1

        # case if theres one last plant in the middle
        if l == r:
            # whichever has more water tries to water it
            if max(capacityA, capacityB) < plants[l]:
                refill += 1

        return refill

        # T O(n) S O(1)