class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()

        n = len(citations)
        l,r = 0,n-1

        while l<=r:
            mid = (l+r)//2

            # check if we found h-index
            if (n-mid) == citations[mid]:
                return n - mid

            # prune search space 
            if (n-mid) < citations[mid]:
                r = mid -1
            else:
                l = mid+1

        return n - l