from collections import deque
class Solution:
    def longestPalindrome(self, s: str) -> str:
        """

        "babad"
         ^
              ^

        expand from the center to build our palindrome substring
        expand the substring regardless if the initial length is odd or even, check both
        """
        # two pointers to expand string from the center
        def expand(i,j):
            l,r = i,j
            
            # expand from center to detect if its a palindrome
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1

            return r - l - 1 # return length of substring once no more matching palindromes

        result = [0,0]

        for i in range(len(s)):
            # consider odd length palindromes
            odd = expand(i,i)

            # check if this is the greatest len
            if odd > result[1] - result[0] + 1:
                # get the num of characters on each side of the palindrome ( for odd)
                dist = odd//2
                result = [i-dist,i+dist] # update current result arr

            # consider even length palindromes
            even = expand(i,i+1)

            # check if this is the greatest len
            if even > result[1] - result[0] + 1:
                # get the num of characters on each side of the palindrome ( for even)
                dist = (even//2) - 1
                result = [i - dist, i + 1 + dist] # update current result arr

        i,j = result # parse from result list and return 

        return s[i:j+1]

        # T O (n^2) S O(1)