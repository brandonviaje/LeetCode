class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.

        both arrays are always sorted in increasing order

        since they are sorted in increasing order, build the list backwards, always put the max out of the two at the back
        shift ptr depending on what is bigger 

        [1,1, 2, 2, 3,3]
         ^
           ^
        [1,2,3]
         ^
        """

        p1 = m - 1
        p2 = n -1
        p = len(nums1) - 1

        # build array backwards, extract max 
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p -= 1
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p -= 1
                p2 -= 1

        # add the leftover numbers in p2
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p -= 1
            p2 -= 1

        


