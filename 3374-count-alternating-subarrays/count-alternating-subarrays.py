class Solution(object):
    def countAlternatingSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        """
        sliding window approach since we need to keep track of subarrays

        create a counter variable so that we can keep track of all the valid alternating ubarrays

        reset window if nums[r] == prev num, set l = r

        increment result and pointer

        [0,1,0,1]
         ^
         ^
        result: 1
        prev: 

        sub optimal: brute force sliding window approach
        optimal: dynamic programming approach

        let d[i] be the number of alternating subarrays ending at index i

        d[i] = d[i-1] + 1

        """
        result = 1
        current = 1

        for i in range(1,len(nums)):
            # check if an alternating subarr
            if nums[i] != nums[i-1]:
                current += 1 
            else:
                current = 1 # reset back to 1

            result += current  # update result

        return result