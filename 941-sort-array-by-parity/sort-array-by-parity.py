class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        """
        intuition:
        two pointers
        - swap if something is even
        - then update the pointer after

        [2,4,3,1]
           ^
               ^
        """

        def isEven(num):
            return num%2 == 0

        swap = 0

        for i in range(len(nums)):
            if isEven(nums[i]):
                nums[i],nums[swap] = nums[swap],nums[i]
                swap += 1
            
        return nums