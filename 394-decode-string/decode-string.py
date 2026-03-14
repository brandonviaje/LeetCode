class Solution:
    def decodeString(self, s: str) -> str:
        """
        looks like basic calculator problem, there can be encoded_str within an encoded_str
        we can use a stack to keep track of the number before '[', 

        check if current num .isdigit(), then add it to our num
        if we encounter a '[', we can recurse to get the str inside the brackets.

        we also have a global result that builds this str for us

        "3[a]2[bc]"
            ^

        []
        num = 3
        """

        def decode(index):
            stack = []
            num = 0

            while index < len(s):
                c = s[index]
                
                # add digit to num
                if c.isdigit():
                    num = num*10 + int(c)
                elif c == '[':
                    temp, index = decode(index + 1) # get temp str and update index
                    stack.append(temp * num)        # add temp str * num
                    num = 0
                elif c == ']':
                    return "".join(stack), index # return str and index u left off at
                else:
                    stack.append(c) # add char to stack 

                # update ptr
                index += 1

            return "".join(stack)

        result = decode(0)
        return result
