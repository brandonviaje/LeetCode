class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        """
        return the number of vowel substrings in word

        we can keep track of the remaining vowels and the seen vowels so that we know
        when to count a vowel substring

        once we encounter a vowel substr, we keep going until we dont end up on a vowel again
        the str len has to be >= 5

        cuaieuouac
         ^
                 ^

        {}
        {u,a,i,e,u,o}
        result = 3
        flag = T

        need to check if its seen already
        need to check if its in vowels
        need to check if flag is True and curr is a idx is a vowel
        need to check if len(set) == 5, that means we found a vowel substr
        """

        result = 0

        for l in range(len(word)):
            vowels = {'a','e','i','o','u'}
            vowel_substr = False
            seen = set()

            # check if idx is a vowel
            if word[l] in vowels:
                r = l
                while r < len(word):
                    # check if already a vowel substr
                    if vowel_substr and word[r] in seen:
                        result += 1

                    # check if in seen
                    if word[r] in seen:
                        r += 1
                        continue

                    # check if in vowels
                    if word[r] in vowels:
                        vowels.remove(word[r])
                        seen.add(word[r])
                    else:
                        break

                    # check if vowel susbtr and havent found a vowel substr yet
                    if len(seen) == 5 and not vowel_substr:
                        result += 1
                        vowel_substr = True

                    r += 1

        return result
                
