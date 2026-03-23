class Solution:
    def myPow(self, x: float, n: int) -> float:
        """
        brute force: use recursion and use n multiplications

        optimal: use binary exponentiation to reduce it to logn multiplications
        """

        def binary_exp(x,n):
            # base case
            if n == 0: return 1
            if n < 0: return 1 / binary_exp(x,-1 * n)

            # if n odd, binary exp on n-1
            if n % 2 == 1:
                return x * binary_exp(x * x, (n-1) // 2)
            else:
                return binary_exp(x*x, n // 2)

        return binary_exp(x,n)