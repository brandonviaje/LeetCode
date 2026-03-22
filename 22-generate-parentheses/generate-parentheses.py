class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def backtrack(num_open,num_close,path):
            # base case
            if num_open == num_close == n:
                result.append("".join(path))
                return

            # add open bracket
            if num_open < n:
                path.append('(')
                backtrack(num_open+1,num_close,path)
                path.pop()

            # if close bracket < open we can add another one
            if num_close < num_open:
                path.append(')')
                backtrack(num_open,num_close+1,path)
                path.pop()

        backtrack(0,0,[])
        return result