class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        boundary = 0
        result = 0

        for num in nums:
            # add to boundary first
            boundary += num

            # if boundary ever is zero that means ant is on it
            if boundary == 0:
                result += 1

        return result