class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        map = {}  # Stores the next greater element for nums2
        result = []

        # Build the mapping from each number in nums2 to its next greater element
        for num in nums2:
            while stack and num > stack[-1]:
                prev = stack.pop()
                map[prev] = num
            stack.append(num)

        # Build the result for nums1 using the map
        for num in nums1:
            result.append(map.get(num, -1)) #default is -1, indicating no bigger element

        return result

        