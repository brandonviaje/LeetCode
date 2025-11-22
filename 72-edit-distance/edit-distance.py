class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """

        if there empty word1: len(word2)
        if there empty word2: len(word1)

        minimum number of operations:
        
        if the characters match: (i+1,j+1)

        insert the character (i,j+1)
        delete a character (i+1,j)
        replace a character (i+1,j+1)
        """

        if word1 == word2:
            return 0

        memo = {}
        def DP(i,j):

            if (i,j) in memo:
                return memo[(i,j)]
            # base case
            if i == len(word1):
                memo[(i,j)] = len(word2)-j
                return memo[(i,j)] 
            if j == len(word2):
                memo[(i,j)] = len(word1)- i
                return memo[(i,j)]

            if word1[i] == word2[j]:
                memo[(i,j)] = DP(i+1,j+1)
            else:
                memo[(i,j)] = 1 + min(DP(i+1,j), DP(i,j+1), DP(i+1,j+1))

            return memo[(i,j)]

        return DP(0,0)