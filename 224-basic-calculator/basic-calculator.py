class Solution:
    def calculate(self, s: str) -> int:
        """
        basically implement a calculator that evaluates a string
        since order of operations matter, we will need to handle ()

        - can be unary or binary since (-1,-2, 2 - 1, etc)

        idea: 
        - if we come across a '(', we should recurse on that part so that we can evaluate that portion of the string first
        - our base case would be if we encounter a ')', then we return the evaluated operation back into a string
        - also if we come across a space ' ', we can just continue

        to handle the actual operations, we can use a stack to keep track of the numbers, and if we come across an operator 
        we have to either check if its unary or binary. if its binary we perform the operation maybe on the stack?

        to check if its a unary operator, i guess we check if s[i-1] is a number, if its not then assume unary operator
        if its not then we do a binary operation


        will also have to handle multi digits, can parse using ptrs

        (1+(11)-3) + (14)
                       ^

        [4,]
        [1]

        since there can be spaces have to skip until we get a number

        1 + 1
            ^
        [2]

        " 2-1 + 2 "
              ^
        [3]

        "(1+(4+5+2)-3)+(6+8)"
                      ^
        [9]
        """
        def evaluate(index):
            stack = []
            num = 0
            sign = 1 # 1 = +, -1 = -

            while index < len(s):
                c = s[index]

                # handle numbers
                if c.isdigit():
                    num = num*10 + int(c)
                elif c == '+':
                    stack.append(sign * num)
                    num = 0
                    sign = 1
                elif c == '-':
                    stack.append(sign * num)
                    num = 0
                    sign = -1
                elif c == '(':
                    num, index = evaluate(index + 1)
                elif c == ')':
                    stack.append(sign * num)
                    return sum(stack), index
        
                # skip space
                index += 1
            stack.append(sign * num)
            return sum(stack),index

        result, _ = evaluate(0)
        return result