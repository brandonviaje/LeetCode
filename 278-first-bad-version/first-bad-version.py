# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        """
        - want to find the very first  bad version of product
        - given n version
        - binary search to minimize num of API calls
        - if mid is >= right and isBadVersion() set that as result
        """


        """
        how to find the very first bad version?
        - Use API call to check if its bad
        - binary search to minimize runtime

        bad = 2
        1 2 3 4 5 6 7
              ^
        """
        result = 0
        prevVersion = 0
        l,r = 1,n

        while l<r:
            mid = (l+r)//2

            if isBadVersion(mid):
                r = mid
            else:
                l = mid + 1

        return l