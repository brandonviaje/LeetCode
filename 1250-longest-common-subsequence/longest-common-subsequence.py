class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # bottom up DP

        n = len(text1)
        m = len(text2)

        # initialize table
        table = [[0 for j in range(m+1)] for i in range(n+1)]

        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                if text1[i] == text2[j]:
                    # add its diagonal (where already precomputed solutions are)
                    table[i][j] = 1 + table[i + 1][j + 1]
                else:
                    # explore down or right 
                    table[i][j] = max(table[i + 1][j], table[i][j+1])

        return table[0][0]