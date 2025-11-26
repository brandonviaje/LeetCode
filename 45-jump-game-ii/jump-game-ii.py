class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        each elements represent max length of a jump

        that means you can jump from 0 to nums[i] forward.
        i+j < n
        0<=j<=nums[i]

        want minimum number of jumps to reach index n-1.

        base case:
        if index == n-1: return count

        brute force:
        - generate all possible combinations of j moving forward.
        - backtrack approach


        optimal solution:
        - dynamic programming looks feasible here
        
        recurrence relation:
        - min_step = min(min_step, 1 + DP(index + step)) <-- override minimum everytime trying out new step
        """

        memo = {}

        def DP(index):
            # base case: go past last index or you are at the very end
            if index >= n-1:
                return 0

            if index in memo:
                return memo[index]

            min_steps = float('inf')
            max_step = nums[index]

            for step in range(1,max_step+1):
                # check if this will take you outta bounds
                if index + step < n:
                    # either take this step, or skip
                    min_steps = min(min_steps, 1 + DP(index + step))

            # store min step into cache
            memo[index] = min_steps
            return memo[index]

        n = len(nums)
        # start at index 0
        return DP(0)
        