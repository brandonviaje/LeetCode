class Solution:
    def reverseWords(self, s: str) -> str:
        """
        "I love u"
                ^
                R
                L
        """
        l,r,scan = 0,0,0
        
        res = ""

        while scan < len(s):

            if s[scan] == " ":
                r = scan - 1
                while r >= l:
                    res += s[r]
                    r -= 1
                
                res += " "
                l = scan + 1

            scan += 1

        r = len(s)-1
        
        while r >= l:
            res += s[r]
            r-= 1

        return res