class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        find longest common subseq. 

        convert nums to set, then check if we are at the start of a subsequence, that means there is val that is 1 less
        """

        nums = set(nums)
        LCS = 0
        for num in nums:
            # check if we are at the start of an LCS
            if num-1 not in nums:
                length = 0
                while(num+length) in nums:
                    length += 1

                LCS = max(LCS,length)

        return LCS
