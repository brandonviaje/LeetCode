class Solution:
    def reverseVowels(self, s: str) -> str:
        #convert to list cause str immutable
        s = list(s)
        vowels = ['a','e','i','o','u']

        #initialize pointers
        left = 0
        right = len(s) - 1

        while left < right:
            #if both pointers are on vowels swap em 
            if s[left].lower() in vowels and s[right].lower() in vowels:
                s[left],s[right] = s[right],s[left]
                #move pointers
                left += 1
                right -= 1
            else:
                # this shifts the pointers until its on a vowel
                while s[left].lower() not in vowels and left < right:
                    left += 1

                while s[right].lower() not in vowels and left < right:
                    right -= 1
           
        

        return "".join(s)

        # T O(n) S O(n)