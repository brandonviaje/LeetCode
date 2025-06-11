class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # build the array backwards since it's sorted
        p1 = m - 1
        p2 = n - 1
        p = len(nums1) - 1

        #while there are still elements to place
        while p1 >= 0 and p2 >= 0:
            #start with the max values at the end of the array 
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1 #move nums1 pointer to the left
            else:
                nums1[p] = nums2[p2]
                p2 -= 1 #move nums2 pointer to the left

            p -=1 #move the main pointer after

        #remaining elements of nums2 copy them over
        while p2>= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -=1

        # T O(m + n) S O(1)
        """
        Where m is the length of nums1 and n is the length of nums2
        O(1) memory because it is in place
        """