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
        ptr = 0
        i = 0
        
        while i < len(abbr):
            # check if character is a num
            if abbr[i].isdigit():
                start = i

                # check if leading zero
                if abbr[i] == "0":
                    return False

                # check if there are numbers ahead
                while i < len(abbr) and abbr[i].isdigit():
                    i += 1
                
                num = int(abbr[start:i]) # get current num to skip
                
                # check if remaining is > word
                if ptr + num > len(word):
                    return False
            
                ptr += num # advance ptr n times
            else:
                # check if ptrs are on same letter or if ptr overflow
                if ptr >= len(word) or word[ptr] != abbr[i]:
                    return False

                #  update ptrs
                i += 1
                ptr += 1

        return ptr == len(word) # check if we sucessfully made it to the end