class Solution:
    def longestValidParentheses(self, s: str) -> int:
        """
        we are given a string with (, ) and have to return 
        length of longest valid parentheses substring

        longest valid parentheses: there is a closed parentheses for each open parentheses that appears

        we can use a stack to track the last invalid position and also index of unmatched '(', 
        to compute the length of valid substrings ending at each index.
        """

        stack = [-1]
        result = 0

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                idx = stack.pop()  # try to match a previous '('

                # if stack not empty, we have a valid substring ending at i
                if stack:
                    result = max(result, i - stack[-1]) 
                else:
                    stack.append(i)                     # make this the new invalid starting point

        return result
