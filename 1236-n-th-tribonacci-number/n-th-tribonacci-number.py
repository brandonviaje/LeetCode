class Solution:
    
    def __init__(self):
        self.memo = {}
    def tribonacci(self, n: int) -> int:

        # CHECK IF ALREADY COMPUTED
        if n in self.memo:
            return self.memo[n]
        # BASE CASES
        if n == 0:
            return 0
        if n <= 2:
            return 1

        # RECURRENCE RELATION
        self.memo[n] = self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)
        return self.memo[n]

