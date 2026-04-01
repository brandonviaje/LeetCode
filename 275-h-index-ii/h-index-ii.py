class Solution:
    def hIndex(self, citations: List[int]) -> int:
        """
        h-index is the max val of h that has published >= papers that have been cited >= h times

        if we get how many papers have been cited using len(citations) - mid == citations[mid],
        then that would be the largest value as shrinking the search space would just make the 
        length smaller

        """

        n = len(citations)
        l,r = 0, n-1

        while l<=r:
            mid = (l+r)//2

            # find h index
            if (n - mid) == citations[mid]:
                return n - mid

            # change search space if we haven't found h-index
            if (n-mid) < citations[mid]:
                r = mid -1
            else:
                l = mid + 1

        return n - l