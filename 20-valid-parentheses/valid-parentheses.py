class Solution:
    def isValid(self, s: str) -> bool:
        """
        we can use a stack when we iterate through the string to process the closing bracket
        hashmap to map open bracket to close. this helps us process the most recent bracket

        the open bracket either must have another open bracket within it or the same closing bracket

        ([])
        ^

        stack = [ (, [ ]
        """

        hashmap = {'(' : ')', '{' : '}', '[' : ']'}

        stack = []
        for char in s:
            # check if current character is an open bracket, add to stack and continue to next char
            if char in "([{":
                stack.append(char)
                continue

            if not stack:
                return False
            
            if char not in hashmap[stack.pop()]: # check if next char is closed bracket for current open bracket
                return False
            
        # return true if we were able to process all parentheses
        return len(stack) == 0


            
