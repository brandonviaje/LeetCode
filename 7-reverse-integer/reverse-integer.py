class Solution:
    def reverse(self, x: int) -> int:
        negative = False

        # check if num is negative
        if x < 0:
            negative = True
            x *= -1 # set to positive

        result = 0

        # add digits to int in reverse
        while x > 0:
            digit = x % 10
            x //= 10

            # check for int overflow
            if(result > (2 ** 31-1)// 10) or (result== (2**31- 1)//10 and digit > 7):
                return 0

            result = result * 10 + digit # add digit to result

        return -result if negative else result 