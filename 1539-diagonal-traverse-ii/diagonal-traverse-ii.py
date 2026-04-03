class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        """
        every number on the pos diag all share the same row + col val

        we can traverse the 2d arr and add the numbers mapped to the same diagonal
        then we can build the list using our dict
        """
        diag = defaultdict(list)
        for row in range(len(nums)):
            for col in range(len(nums[row])):
                diag[row+col].append(nums[row][col])

        result = []

        for key,nums in diag.items():  
            # build result list
            while nums:
                result.append(nums.pop())
 

        return result