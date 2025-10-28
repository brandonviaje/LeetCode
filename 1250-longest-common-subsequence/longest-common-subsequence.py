class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}

        def DP(index1,index2):
            # store precomputed solution
            if (index1,index2) in memo:
                return memo[(index1,index2)]

            # if out of bounds return 0
            if index1 >= len(text1) or index2 >= len(text2):
                return 0

            # if we find matching chars, find the LCS of the smaller substring not including this character
            if text1[index1] == text2[index2]:
                memo[(index1,index2)] = 1 + DP(index1+1,index2+1)
            else: # we did not find any matching, explore the substrings
                memo[(index1,index2)] = max(DP(index1+1,index2),DP(index1,index2+1))

            return memo[(index1,index2)]

        return DP(0,0)
            