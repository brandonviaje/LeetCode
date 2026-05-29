class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        """
        start with word1 and word2, keep adding until one word runs out

        check what word still has leftovers and add the rest to our result

        abc
          ^
        pqr
          ^

        "apbqcr"

        ab
          ^
        pqrs
          ^
        
        "apbqrs"
        """

        idx_1 = 0
        idx_2 = 0

        result = ""

        while idx_1 < len(word1) and idx_2 < len(word2):
            result += word1[idx_1]
            result += word2[idx_2]

            # update ptr
            idx_1 += 1
            idx_2 += 1

        
        # add the leftover from both words
        while idx_1 < len(word1):
            result += word1[idx_1]

            # update ptr
            idx_1 += 1

        while idx_2 < len(word2):
            result += word2[idx_2]

            # update ptr
            idx_2 += 1

        return result