class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        """
        this is basically finding the LCS but with numbers. We dont want any line we connect to intersect, so its like a subsequence.
        """
        m = len(nums1)
        n = len(nums2)

        # create the DP table
        dp = [[0 for j in range(n + 1)] for i in range(m + 1)]

        print(dp)
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if nums1[i] == nums2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])

        return dp[0][0]