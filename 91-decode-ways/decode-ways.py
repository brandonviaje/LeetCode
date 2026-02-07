class Solution:
    def numDecodings(self, s: str) -> int:
        """
        two ways to check how many ways we can decode this
        
        we can either
        - decode the first digit DP(i)
        - decode two digits consecutively DP(i+2)

        DP(index) = number of ways to decode s[index:]

        we need to check if the first digit is a 1 or 2 and then the second digit is 0,1,2,3,4,5,6

        add to the result based on the amount of times we can decode
        """

        memo = {len(s) : 1}

        def DP(index):
            # check if sol already stored
            if index in memo:
                return memo[index]

            if s[index] == "0":
                return 0

            result = DP(index+1)  # we can decode 1 digit

            # check if we can decode 2 digits consecutively
            if index + 1 < len(s) and 10 <= int(s[index:index+2]) <= 26:
                result += DP(index + 2)

            memo[index] = result
            return result

        return DP(0)