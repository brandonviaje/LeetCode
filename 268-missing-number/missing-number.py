class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        seen = set()

        # add to seen set to figure out the missing number
        for i in range(n+1):
            seen.add(i)

        # iterate through the array , remove each number, you will be left with last one
        for num in nums:
            seen.remove(num)

        return next(iter(seen))

        # T O(n) S O(n)

            
        