class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """


        """
        intuition:
        - we can find how to do this by taking the left max and the right max
        - you can find the max of the difference of the left pointer and the leftMax
        """

        l,r = 1,len(height)-2
        lMax = height[l - 1]
        rMax = height[r + 1]
        result = 0

        while l<=r:
            # if the rMax is > lMax
            if rMax <= lMax:
                result += max(0, rMax - height[r])
                rMax = max(rMax, height[r])
                r -= 1
            else:
                result += max(0, lMax - height[l])
                lMax = max(lMax, height[l])
                l += 1

        return result

        # T O(n) S O(1)