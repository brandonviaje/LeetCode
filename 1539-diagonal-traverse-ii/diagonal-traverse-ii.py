class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        """
        what i notice: 
        - when traversing it goes from bottom left to bottom right
        - it can be different sizes
        - values along the same diagonal all add up to the same index
        - make a hashmap to capture all elements and store em
        - after create a result array
        """

        track = defaultdict(list)

        # map index sum values and list of nums
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                track[i + j].append(nums[i][j])

        res = []
        
        # go through each list and add the reversed 
        for k,v in track.items():
            for num in reversed(track[k]):
                res.append(num)
        
        return res