class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        ideas: hashmap, two pointers

        array is sorted in increasing order already

        [1,1,2,2,2,3,3]
                   ^
                 ^
         {1: 2, 2:2}

         use a  hashmap to keep track of freq
        """

        freq = defaultdict(int)
        unique = 0

        for i in range(len(nums)):
            # if freq already at max, don't swap
            if freq[nums[i]] == 2:
                continue

            # increase freq, swap values and update ptr
            freq[nums[i]] += 1
            nums[i],nums[unique] = nums[unique],nums[i]
            unique += 1

        return unique