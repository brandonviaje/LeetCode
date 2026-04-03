class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        """
        sort the weight array, to get smaller weights first
        we want to get smaller weights first so that we can get as much apples in the basket
        """

        weight.sort()
        total = 0
        count = 0

        for w in weight:
            if total + w > 5000:
                break

            total += w
            count += 1

        return count