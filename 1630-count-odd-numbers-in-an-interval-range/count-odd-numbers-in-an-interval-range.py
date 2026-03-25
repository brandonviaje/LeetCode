class Solution:
    def countOdds(self, low: int, high: int) -> int:
        """
        idea: traverse low all the way to high and check for an odd num, increment result

        divide and conquer approach, split halfway and check how many numbers is odd in each partition
        """

        # O(1)
        return ((high + 1) // 2) - (low // 2)