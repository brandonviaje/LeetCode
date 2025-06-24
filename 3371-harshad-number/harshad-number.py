class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        
        xStr = str(x)
        digitSum = 0

        for c in xStr:
            digitSum += int(c)

        if x % digitSum == 0:
            return digitSum
        else:
            return -1