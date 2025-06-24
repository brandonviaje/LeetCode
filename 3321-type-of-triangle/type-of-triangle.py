class Solution:
    def triangleType(self, nums: List[int]) -> str:
        countSides = Counter(nums)
        
        # check if can form triangle
        if not (nums[0] + nums[1] > nums[2] and nums[0] + nums[2] > nums[1] and nums[1] + nums[2] > nums[0]):
                return "none"
        else:      
            if len(countSides) == 3:
                return "scalene"
            elif len(countSides) == 2:
                return "isosceles"
            elif len(countSides) == 1:
                return "equilateral"