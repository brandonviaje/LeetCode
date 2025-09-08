class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        """ 
        backtracking boiler plate


        1. base case

        2. make a choice

        3. recurse

        4. backtrack/undo

        """

        # either we choose to take the number, or we dont

        def backtrack(index,path):
            result.append(path[:])
            # base case, we are at the end of the array
            if index == len(nums):
                # add to result
                return

            # iterate through nums
            for i in range(index, len(nums)):
                
                # skip through any duplicates
                if i > index and nums[i] == nums[i-1]:
                    continue

                # add to decisions array
                path.append(nums[i])
                # recurse
                backtrack(i+1,path)
                path.pop()
        
        # O n log n
        nums.sort()
        result = []
        backtrack(0,[])
        return result

        
        