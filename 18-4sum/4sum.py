class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        [1,0,-1,0,-2,2]
        target = 0
        [-2,-1,0,0,1,2]
          ^
             ^
               ^
                 ^

        two for loops to check each combination, but two pointers to scan through the other
        sort the array first
        if its > target decrement right 
        if its < target increment left


        [-2,-1,-1,1,1,2,2]
             ^
                ^
                  ^ ^
                    
                    
        """
        nums.sort()
        result = []

        for i in range(len(nums)):
            # skip dupes
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            for j in range(i+1,len(nums)):
                # skip dupes
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue

                left = j + 1
                right = len(nums)-1

                while left < right:
                    fourSum = nums[i] + nums[j] + nums[left] + nums[right]

                    if fourSum == target:
                        # store result
                        result.append([nums[i],nums[j],nums[left],nums[right]])

                        # update pointer after
                        left += 1
                        right -= 1
                        
                        # skip dupes
                        while left < right and nums[left] == nums[left-1]:
                            left += 1
                        while left < right and nums[right] == nums[right+1]:
                            right -= 1

                    elif fourSum > target:
                        right -= 1
                    else:
                        left += 1

        return result

        # T O(n^3) S O(k)
        # k is all unique quadruplets