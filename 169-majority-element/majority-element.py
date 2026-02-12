class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = Counter(nums)

        majority = 0
        maxFreq = 0

        # iterate throug hashmap
        for num, freq in hashmap.items():

            maxFreq = max(maxFreq,freq) # get max freq

            # if freq == maxFreq set majority to key
            if freq == maxFreq:
                majority = num

        return majority