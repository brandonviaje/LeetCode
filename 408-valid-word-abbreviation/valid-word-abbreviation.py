class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        """
        return if word matches abbreviation, can't have a leading 0

        check for valid abbreviations:

        scan for trailing zeroes

        iterate through abbreviations, and have a pointer that keeps track of word

        when we encounter a digit in the string, we need to check if it a leading 0 or if the number is greater than the string, this would make it an invalid abbreviation
        
        if we are able to make it through the loop of abbreviations without return false, then it must be a valid abbreviation for that word
        """
        i,j = 0,0
        while j < len(abbr):
            num = 0

            # check if abbr has digits
            if abbr[j].isdigit():
                if abbr[j] == '0':
                    return False

                while j < len(abbr) and abbr[j].isdigit():
                    num = num * 10 + int(abbr[j]) # build num
                    j += 1

                if i + num > len(word):
                    return False

                i += num # update curr ptr
            else:
                if i >= len(word) or word[i] != abbr[j]:
                    return False
            
                # update ptr
                i += 1
                j += 1

        return i == len(word) # check if we reached the end of word