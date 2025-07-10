class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
        cost[i] amount of gas it takes to travel to next
        gas[i] how much gas there is
        gas:
        [1,2,3,4,5]
         ^
        cost:
        [3,4,5,1,2]
         ^
        - check if fuel - cost + fuel at next station >= 0 => we can go
        - if we ever are at <0 continue iteration
        fuel =  8 - 2 + 1 = 7
        """
        # if sum of gas < sum of cost they cant make it in a circle
        if sum(gas) < sum(cost):
            return - 1

        # there exists a solution since theres enough gas to make a round trip
        total= 0
        result = 0

        for i in range(len(gas)):
            # calculate total and check if its less than 0
            total += (gas[i]-cost[i])

            if total < 0:
                # reset back to zero
                total = 0
                result = i + 1 # everything from result to i didnt work, so set result as the next ith station to test
        
        return result

        # T O(n) S O(1)