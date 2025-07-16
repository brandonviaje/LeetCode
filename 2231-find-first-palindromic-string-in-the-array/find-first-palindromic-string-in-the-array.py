class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        def pal(word):
            left,right = 0,len(word)-1
            while left<right:
                if word[left] != word[right]:
                    return False
                left += 1
                right -= 1
            return True

        for word in words:
            if pal(word):
                return word

        return ""