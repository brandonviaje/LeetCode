class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        """
        greedy approach

        sort array be price_A - price_B representing the company's additional cost

        send first n persons with smallest price_A - price_B to city A, and then the rest to city B
        """
        n = len(costs) // 2
        result = 0 
        costs.sort(key = lambda x : x[0]-x[1]) # sort in asc order by price_A - pirice_B

        # send first N ppl to city A    
        for i in range(n):
            result += costs[i][0]

        # send the rest to city B
        for i in range(n,len(costs)):
            result += costs[i][1]

        return result