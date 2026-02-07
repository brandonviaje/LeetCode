class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        build palindromic substring outwards, check each character and build substring outwards

        babad
         ^
           ^
        
        if size of curr substring (r-l+1) > len(result), update result
        """

        resIdx = 0
        resLen = 0

        for i in range(len(s)):
            # odd len string
            l,r = i,i

            while l>=0 and r < len(s) and s[l] == s[r]:
                # check if curr str > prev res, update if it is
                if(r-l+1) > resLen:
                    resIdx = l
                    resLen = (r-l+1)
                # expand outwards
                r += 1
                l -= 1

            # even len string
            l,r = i, i+1
            
            while l>=0 and r < len(s) and s[l] == s[r]:
                # check if curr str > prev res, update if it is
                if(r-l+1) > resLen:
                    resIdx = l
                    resLen = (r-l+1)
                
                # expand outwards
                r += 1
                l -= 1

        return s[resIdx:resIdx +resLen] # return substring of longest palindrome

        # T O(n)
        # S O(n)