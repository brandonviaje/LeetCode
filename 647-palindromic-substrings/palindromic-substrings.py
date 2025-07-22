class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        intuition:

        - every character is a palindrome by itself, so we start at 0 and add 1 whenever we find a valid one.
        - we iterate through the string to solve the subproblems s
        - instead of checking every possible substring, we can expand from the center outwards.
        - if the characters on the left and right are the same, it’s a palindrome. we add 1 to the result and keep expanding.

        why check both odd and even lengths?

        - palindromes can have:
            - odd length: center is a single character ("racecar")
            - even length: center is between two characters ("abba")
        - so for each index, we do two checks:
            - expand from (i, i) → for odd-length palindromes
            - expand from (i, i + 1) → for even-length palindromes

        - each center is like a mini problem (dynamic programming):
            - how many palindromes can u find if i expand from here

        brute force: generate all substrings and check each one (O(n^3))
        """

        result = 0

        def pal(word,l,r):
            count = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
            return count

        for i in range(len(s)):
            # check for odd length pal
            result += pal(s,i,i)
            # check for even length pal
            result += pal(s,i,i+1)

        return result

        # T O(n^2) S O(1)