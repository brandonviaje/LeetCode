class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        given a wildcard pattern, we want to check if that string can match the pattern

        - if pattern is *, it can match any sequence of chars
        - if pattern is '?', we can match it
        - if pattern of p[i] == s[i], we can match that also

        DP problem, our subproblems consist of traversing the idx pointers if we get a match or if p[i] == '?'
        we have to handle the kleene star. I think if there is * present in anything, then we can return True

        DP[(i,j)] = DP(i+1,j+1) if s[i] == s[j]
        DP[(i,j)] = DP(i)

        """
        new_p = []
        # collapse repetitive kleene stars
        for c in p:
            if not new_p or c != '*' or new_p[-1] != '*':
                new_p.append(c)

        p = "".join(new_p)
        memo = {}
        def DP(i,j):
            # check if precomputed solution also
            if (i,j) in memo:
                return memo[(i,j)]

            # base cases
            if i >= len(s) and j >= len(p):
                return True
            if j >= len(p):
                return False
            if i >= len(s):
                memo[(i,j)] = all(x == '*' for x in p[j:])
                return memo[(i,j)]
                
            # handle kleene star
            if p[j] == "*":
                memo[(i,j)] =  ((i+1 < len(s) and DP(i+1,j)) or DP(i,j+1)) or DP(i+1,j+1)
                return memo[(i,j)]

            # check for a match
            if (s[i] == p[j] or p[j] == '?'):
                memo[(i,j)] = DP(i+1,j+1)
                return memo[(i,j)]

            memo[(i,j)] = False # store state
            return False    

        return DP(0,0)