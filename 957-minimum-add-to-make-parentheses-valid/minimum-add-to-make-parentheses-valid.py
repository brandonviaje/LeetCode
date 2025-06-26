class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        result = 0
        stack = []
        
        for c in s:
            if c == '(':
                stack.append(c)
            else:
                if stack:
                    stack.pop()
                else:
                    result += 1

        return result + len(stack)

        """
        "())"
           ^  
        []
        result = 1
        return: 1

        "((("
         ^
        [(,(,(]
        result = 0
        return : 3
        """