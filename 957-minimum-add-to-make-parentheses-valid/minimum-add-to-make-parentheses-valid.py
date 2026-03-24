class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        needed = 0

        for ch in s:
            if ch == ")":
                if stack:
                    stack.pop()
                else:
                    needed += 1
            else:
                stack.append(ch)

        return len(stack) + needed