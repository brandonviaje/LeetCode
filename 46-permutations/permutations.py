class Solution:
    
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(index,path):
            #base case
            if len(path) == len(nums):
                # build result
                result.append([elem for elem in path])
                return

            for i in range(index,len(nums)):

                nums[index], nums[i] = nums[i], nums[index]   # choose number to build from
                path.append(nums[index])
                backtrack(index+1,path) # recurse

                # backtrack
                nums[index], nums[i] = nums[i], nums[index]   
                path.pop()

        backtrack(0,[])
        return result