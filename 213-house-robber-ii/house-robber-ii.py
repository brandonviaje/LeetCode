class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        simulate the max amount of money you can take through 0 to n-2 and 1  to n-1
        subproblem find the biggest cost of robbing current house then next, or skipping and stealing next
        """

        if(len(nums) == 1):
            return nums[0]

        def robHouse(start,end):
            memo = {}
            def DP(index):
                if index in memo:
                    return memo[index]
                if index > end:
                    return 0

                memo[index] = max(nums[index] + DP(index+2), DP(index+1))
                return memo[index]

            return DP(start)

        # simulate first robbing from 0th house to n-2 house,
        # simualte second robbing from 1st house to n-1 house.
        # get max out of the two
        total = max(robHouse(0,len(nums)-2), robHouse(1,len(nums)-1))
        return total
