class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        """
        number of ways to go about this:
        - u can go through the array and if the word in word1 or word2, mark it
        - str can appear more than once, so always track most recent one
        - calc min_distance if both are found (!=-1), and save shortest distance always
        """

        min_dist = float('inf')
        word1_idx = -1
        word2_idx = -1

        for i in range(len(wordsDict)):
            # latest idx if equals to word1
            if wordsDict[i] == word1:
                word1_idx = i

            # latest idx if equals to word2
            if wordsDict[i] == word2:
                word2_idx = i

            # calc min distance if both words seen
            if word1_idx != -1 and word2_idx != -1:
                min_dist = min(min_dist, abs(word2_idx - word1_idx))
                
        return min_dist