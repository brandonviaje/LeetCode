class Solution:
    def mySqrt(self, x: int) -> int:

        left = 0
        right = x
        result = 0
        while left <= right:
            middle = (left + right) // 2

            if middle * middle == x:
                return middle
            elif middle * middle < x:
                result = middle
                left = middle + 1
            else:
                right = middle - 1
        
        return result