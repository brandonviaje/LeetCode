class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        
        i,j = len(num1) - 1, len(num2) - 1
        carry = 0
        result = []

        while i >= 0 or j >= 0 or carry:

            #convert from char to int 
            if i >= 0:
                digit1 = ord(num1[i]) - ord('0') 
            else:
                digit1 = 0

            if j >= 0:
                digit2 = ord(num2[j]) - ord('0')
            else:
                digit2 = 0

            #calculate total
            total = digit1 + digit2 + carry

            # carry if total is greater than 10
            carry = total // 10
            result.append(str(total%10)) # only last digit

            # update pointers
            i -= 1
            j -= 1

        return "".join(reversed(result)) # reverse the result 
        # T O (n) S O(n)