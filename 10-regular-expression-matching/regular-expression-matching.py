class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}

        def DP(i,j):

            # check if already precomputed
            if (i,j) in memo:
                return memo[(i,j)]

            # base cases
            if (i >= len(s) and j >= len(p)):
                return True
            if (j >= len(p)):
                return False

            match = i < len(s) and (s[i] == p[j] or p[j] == '.')

            # handle kleene star
            if j+1 < len(p) and p[j+1] == "*":
                # check if we have a match so we can move i ptr up
                memo[(i,j)] = ((match and DP(i+1,j)) or DP(i,j+2)) # or use zero occurences of prev character 
                return memo[(i,j)]

            # check for a match
            if match:
                memo[(i,j)] = DP(i+1,j+1)
                return memo[(i,j)]

            return False

        return DP(0,0)