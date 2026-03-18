class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        """
        brute force: try every num up to n if pow(3,i) == n
        - use binary search to reduce search space in time for logn

        prune search space by a third by dividing by 3 log_3(n)
        """
        if n <= 0:
            return False

        # keep dividing by 3 
        while n %3 == 0:
            n //= 3

        return n == 1