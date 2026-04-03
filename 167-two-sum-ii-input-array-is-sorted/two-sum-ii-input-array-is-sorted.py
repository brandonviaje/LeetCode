class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        since the array is sorted and guaranteed a solution
        we can use ptrs to keep track of the curr sum

        if the curr sum is greater than the target, we move the right ptr inwards, if it is less than, 
        then we can move the left ptr inwrads
        """

        l,r = 0,len(numbers)-1

        # find curr sum
        while l < r:
            curr_sum = numbers[l] + numbers[r]

            if curr_sum == target:
                return [l+1,r+1]
            elif curr_sum < target:
                l += 1
            else:
                r -= 1

    