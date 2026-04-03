class Solution:
    def validPalindrome(self, s: str) -> bool:

        if not s:
            return True
        
        l,r = 0 ,len(s)-1

        def isValid(left,right):
            while left < right:
                if s[left] != s[right]:
                    return False
                
                left += 1
                right -= 1

            return True

        while l < r:
            if s[l] != s[r]:
                return isValid(l+1,r) or isValid(l,r-1)

            l += 1
            r-= 1

        return True