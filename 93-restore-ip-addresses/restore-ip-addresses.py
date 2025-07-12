class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        addresses = []
        path = []

        def validNum(s):
            # skip leading zeroes
            if  len(s) > 1 and s[0] == "0":
                return False

            return 0<=int(s)<=255

        def backtrack(index,dots):
            # BASE CASE
            if index == len(s) and dots == 0:
                addresses.append([n for n in path])
                return

            for i in range(index,len(s)):
                # check if its a valid number (0-255)
                if validNum(s[index:i+1]):
                    # ADD TO SOMETHING  
                    path.append(s[index:i+1])

                    # RECURSE
                    backtrack(i+1,dots-1)

                    # UNDO
                    path.pop()

        backtrack(0,4)
        result = []
        
        for add in addresses:
            result.append(".".join(add))

        return result