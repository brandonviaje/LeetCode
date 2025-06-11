class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        # Optimal Solution

        # get sum up to k, starting our window
        windowSum = sum(nums[:k])
        maxAvg = windowSum / k
    
        # change sum as we slide static window down array
        for i in range(k, len(nums)):
            windowSum += nums[i] - nums[i - k]
            maxAvg = max(maxAvg, windowSum / k) # replace with max avg
        
        return maxAvg

        # T O(n) S O(1)

            


            