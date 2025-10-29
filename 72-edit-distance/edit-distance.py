class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """

        need to convert word1 to word2, with three operations
        - insert char
        - delete char
        - replace char

        break this problem down into smaller subproblems.

        base cases:
        - if word1 was empty, return len of word2, if word2 empty return len of word1.
        - if both are empty return 0.

        intuition:
        if we have a matching character word1[i] == word2[j], then our new subproblem is the the substring at index i+1 and j+1.

        else, we have to choose three operations
        - insert
        - delete
        - replace

        insert: if we were to insert a character in word1 with the current pointer of word2, all we would have to do then is increment j. (i,j+1)
        delete: if we delete a character at word1[i], then just increment i. (i+1,j)
        replace: when we replace a character at word1[i] with the char at word1[j] we are done solving that substring. (i+1,j+1).

        Similar to LCS pattern.

        We can build a DP table with our base cases set at the bounds. We build bottom up our optimal result. We know what each operation represents index wise, so when we start from bottom up it'll go to the base cases and solve the bigger problem.

    
        """

        # create the DP table
        DP = [[0 for j in range(len(word2)+1)] for _ in range(len(word1)+1)]

        # insert base case values at edge of table.

        # Build DP table bottom-up
        for i in range(len(word1),-1,-1):
            for j in range(len(word2),-1,-1):
                # fill in our base cases
                if i == len(word1):
                    DP[i][j] = len(word2) - j
                elif j == len(word2):
                    DP[i][j] = len(word1) - i
                # if we have a matching character, focus on the next substring
                elif word1[i] == word2[j]:
                    DP[i][j] = DP[i+1][j+1]
                # choose optimal solution from the DP table
                else:
                    DP[i][j] = 1 + min(DP[i+1][j],    # delete
                                    DP[i][j+1],    # insert
                                    DP[i+1][j+1])  # replace

        print(DP)
        return DP[0][0]