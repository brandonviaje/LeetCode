# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        """
        binary search to find the very leftmost index
        perform a binary search on the number itself
        """

        l,r = 0,n
        result = -1

        while l<=r:
            mid = (l+r)//2
            if isBadVersion(mid):
                r = mid - 1
            else:
                l = mid + 1
            if isBadVersion(mid):
                result = mid

        return result