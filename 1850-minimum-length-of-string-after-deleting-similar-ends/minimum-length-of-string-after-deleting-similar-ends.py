class Solution:
    def minimumLength(self, s: str) -> int:
        """
        basically, you have to keep scanning contiguously for equal characters,
        not really a sliding window, but definitely a two pointer problem where you keep going until it isnt equal to the suffix/prefix
        """

        result = len(s)
        l,r = 0 , len(s)-1
        # check if the sequences match
        while l < r and s[l] == s[r]:
            # capture the suffix and prefix
            val = s[r]

            # keep scanning for prefix and suffix until not equal to each other             
            while s[l] == val:
                result -= 1 

                if result == 0:
                    return result
                l += 1

            while s[r] == val:
                result -= 1

                if result == 0:
                    return result
                r -= 1

        return result

        """
        "cabaabac"
           ^
              ^
        res = 6
        """