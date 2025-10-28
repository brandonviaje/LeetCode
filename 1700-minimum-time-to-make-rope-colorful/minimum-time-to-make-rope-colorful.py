class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        total = 0
        prev_cost = neededTime[0]
        n = len(colors)

        # start at second index
        for i in range(1, n):
            # check for a violation
            if colors[i] == colors[i-1]:
                # remove smaller cost balloon
                total += min(prev_cost, neededTime[i])
                # keep the bigger one
                prev_cost = max(prev_cost, neededTime[i])
            else:
                # no conflict, move prev_cost forward
                prev_cost = neededTime[i]

        return total