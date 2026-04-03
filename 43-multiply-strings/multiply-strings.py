class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        """
        build num digit by digit and then multiply both of em
        """

        x = 0
        y = 0

        for i in range(len(num1)):
            x = (x * 10) + int(num1[i])

        for j in range(len(num2)):
            y = (y * 10) + int(num2[j])

        prod = x * y

        return str(prod)