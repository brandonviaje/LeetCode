class Solution:

    """
    two pointer approach scan if its a palindrome from both sides

    if we get a character mismatch, then either shift left pointer or right pointer and check if its a palindrome still
    """
    
    def isPalindrome(self,left,right,s):

        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1

        return True
    
    def validPalindrome(self, s: str) -> bool:
        
        left, right = 0, len(s) - 1

        while left < right:

            # if there is a character mismatch 
            if s[left] != s[right]:
                # check if we move either left or right pointer if we have a valid palindrome still
                return self.isPalindrome(left+1,right,s) or self.isPalindrome(left,right-1,s)

            # else just update pointer
            left += 1
            right -= 1

        return True

        # T O(n) S O(1)
        