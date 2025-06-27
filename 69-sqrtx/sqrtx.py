import math

class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        result = 0
        
        while left <= right:
            mid = (left + right) // 2
            
            if mid * mid== x:
                return mid
            elif ( mid * mid) < x:
                result = mid
                left = mid + 1
            else:
                right = mid - 1
                
        return result

        
        # for i in range(1000):
        #     print(f"A: {endpoint_a} B: {endpoint_b} Midpoint: {midpoint}")

        #     if abs(midpoint * midpoint - target) < epsilon:
        #         return math.floor(midpoint)
        #     elif (midpoint * midpoint) > target:
        #         endpoint_b = midpoint
        #         midpoint = (endpoint_a + endpoint_b) / 2
        #     else:
        #         endpoint_a = midpoint
        #         midpoint = (endpoint_a + endpoint_b) / 2
                