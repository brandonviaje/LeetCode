class Solution:
    def reverseWords(self, s: str) -> str:
        """
        "  hello world  "
         ^
         ^
        """
        l,r = len(s)-1,len(s)-1
        result = []

        while r >= 0:
            # get rid of the trailing spaces
            while s[r] == ' ':
                r -= 1
                l -= 1

            # shift left until we come across a space 
            while l >= 0 and s[l] != ' ':
                l -= 1
            
            if l != r:
                result.append(s[l+1:r+1])
                r = l

        return " ".join(result)

            