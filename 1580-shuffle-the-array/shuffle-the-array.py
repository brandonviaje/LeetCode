class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        
        storeN = []
        store2N = []

        for i in range(n):
            storeN.append(nums[i])

        for i in range(n,len(nums)):
            store2N.append(nums[i])

        for i in range(n):
            nums[2*i] = storeN[i]
            nums[2*i + 1] = store2N[i]
    
        return nums
        