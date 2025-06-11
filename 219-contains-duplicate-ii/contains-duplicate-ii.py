class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

                # Optimal Solution

        seen = set() #O (1) lookup
        
        for i in range(len(nums)):
            # if number found in seen return true, both in same window
            if nums[i] in seen:
                return True

            seen.add(nums[i]) 

            # shrink window if it is over k
            if len(seen) > k:
                seen.remove(nums[i - k])

        return False

        # T O(n) S O (n)

        """
        Brute Force

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j] and abs(i-j) <= k:
                    return True

        return False    

        T O(n^2) S O(1)
        """

