class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        mat = defaultdict(list)

        # group elements by the sum of their indices 
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                mat[i+j].append(nums[i][j])

        result = []

        # reverse the list before adding to the result
        for k,v in mat.items():
            for num in reversed(v):
                result.append(num)

        return result