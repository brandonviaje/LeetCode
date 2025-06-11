class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s = list(s)
        left = 0
        right = len(s) - 1

        while left<right:
            #if pointers are both on alphabet swap
            if s[left].isalpha() and s[right].isalpha():
                s[left], s[right] = s[right],s[left]
                #update pointers after swap
                left+= 1
                right -= 1
            else:
                if not s[left].isalpha(): left += 1
                if not s[right].isalpha(): right -= 1

        return "".join(s)