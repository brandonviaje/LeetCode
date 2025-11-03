class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        """
        Need an optimal, think DP

        Subproblem:
        - Buy a 1 day pass cost[0]
        - Buy a 7 day pass cost[1]
        - Buy a 30 day pass cost[2]

        Choose the pass that minimizes the cost but also is good for the sufficient amount of days

        T(n) be the min num of dollars needed to travel every day in the given list of days

        T(n) = min(T(day + 1, sum + costs[00]),T(day + 7, sum + costs[1]),T(day + 30, sum + costs[2]))
        """

        def find_next_index(start_day):
            i = 0
            # find next index of the days array given start day
            while i < len(days) and days[i] <= start_day:
                i += 1
            return i

        memo = {}
        def dp(index):
            if index in memo:
                return memo[index]

            if index >= len(days):
                return 0
            # recurrence relation
            memo[index] = min(costs[0] + dp(index+1),costs[1] + dp(find_next_index(days[index] + 6)),costs[2] + dp(find_next_index(days[index] + 29)))
            return memo[index]

        return dp(0)