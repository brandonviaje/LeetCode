class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []


        path = path.split("/")

        for part in path:
            # pop from stack if ..
            if part == "..":
                if stack:
                    stack.pop()
            # if empty str or curr dir, continue
            elif part == "." or not part:
                continue
            else:
                # add directory name to stack
                stack.append(part)

        # build final path
        result = "/" + "/".join(stack)
        return result