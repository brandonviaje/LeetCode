class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        """
        backtrack to explore all possible decisions to reach target

        when we find our target sum, we recurse and add that to the result list

        we build our array by building paths, they can either choose to add it or skip it
        if it is greater than target, we can just skip since we dont want that
        backtrack would be terminated by the for loops iteration
        """

        def backtrack(decisions,adder,index):
            # base case
            if adder == target:
                result.append(decisions[:])
                return

            for i in range(index,len(candidates)):
                # if the sum is greater than the target skip this iteration and move to the next
                if adder + candidates[i] > target:
                    continue

                # choose to add to the decisions list
                decisions.append(candidates[i])
                # recurse after and then backtrack is finished here
                backtrack(decisions, adder + candidates[i],i)
                decisions.pop()

        # to get rid of permutations, kill branch when
        result = []
        backtrack([],0,0)
        return result
    