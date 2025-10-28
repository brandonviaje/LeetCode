class Solution:
    
    def rob(self, nums: List[int]) -> int:
        """
        brute force by backtracking the number of ways you can take money
        return the biggest amount

        save computer subproblems

        if you take from first house, cant take from last

        0... n-1
        1 ... n

        T(i) = max money you can take

        T(i) = max(rob(0,n-1),rob(1,n))

        """

        n = len(nums)
        if n == 1:
            return nums[0]
        
        def robRange(arr):
            prev2, prev1 = 0, 0
            
            for num in arr:
                curr = max(prev1, prev2 + num)
                prev2, prev1 = prev1, curr

            return prev1

        # Exclude first house (nums[1:]) or exclude last house (nums[:-1])
        return max(robRange(nums[:-1]), robRange(nums[1:]))