class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i, a in enumerate(nums):
            #skip duplicates
            if i > 0 and a == nums[i-1]:
                continue

            #everything else is a two sum II problem

            left = i + 1
            right = len(nums)-1

            while left < right:
                
                threeSum = a + nums[left] + nums[right]
                if(threeSum > 0):
                    right -= 1
                elif(threeSum < 0):
                    left += 1
                else:
                    #add to list, then move the pointers
                    result.append([a,nums[left],nums[right]])
                    left +=1
                    right -=1
                        
                    #skip duplicates
                    while left<right and nums[left] == nums[left-1] :
                        left +=1
                    while left<right and nums[right] == nums[right+1]:
                        right -=1
        return result