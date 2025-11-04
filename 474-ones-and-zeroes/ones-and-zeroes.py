class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        """
        Subproblem:

        find the maximum subset if we take the current one, or the next one


        let T(n) be the largest subset of strs that satisfy the condition
        T(1) = 1
        T(n) = max(1 + T(n+1), T(n+!))
        """

        # Precompute count of zeros and ones for each string
        counts = []
        for s in strs:
            zeros = s.count("0")
            ones = s.count("1")
            counts.append((zeros, ones))

        memo = {}
        def dp(index,ones,zeros):

            if (index,ones,zeros) in memo:
                return memo[(index,ones,zeros)]
            
            # base case
            if index == len(strs):
                return 0
            
            # get num of zeros and ones of current string
            z,o = counts[index]

            take = 0
            # check if we are meeting our constraint
            if zeros + z <= m and ones + o <= n:
                # take this string and build our subset
                take = 1 + dp(index+1,ones + o,zeros + z)

            # recurrence relation: either skip string, or take it
            memo[(index,ones,zeros)] = max(take, dp(index+1,ones,zeros))
            return memo[(index,ones,zeros)]
                

        return dp(0,0,0)