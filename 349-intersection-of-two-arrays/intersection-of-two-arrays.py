class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """

        [1,2,2,1]  
        
        [2,2]

        notes:
        - find the longer length array
        - go through the longer array add it to a set
        - then iterate through the smaller array and if its in the set add it to result

        """
        result = set()
        if len(nums1) >= len(nums2):
            seen = set(nums1)
            for num in nums2:
                if num in seen:
                    result.add(num)
        else:
            seen = set(nums2)
            for num in nums1:
                if num in seen:
                    result.add(num)
        
        return list(result)
