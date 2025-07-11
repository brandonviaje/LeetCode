class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        """
        abc
           ^
        ahbgdc
             ^
        """

        if not s:
            return True

        p = 0

        for c in t:
            if c == s[p]:
                p += 1

            if p > len(s)-1:
                return True
        # if p pointer is out of bounds/range then you were able to find a subsequence
        return False