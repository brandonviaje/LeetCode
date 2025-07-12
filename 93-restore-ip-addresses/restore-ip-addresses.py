class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        addresses = []
        path = []

        def validNum(s):
            # skip leading zeroes
            if  len(s) > 1 and s[0] == "0":
                return False

            return 0<=int(s)<=255

        def backtrack(index,segmentsLeft):
            # BASE CASE
            if index == len(s) and segmentsLeft == 0:
                addresses.append([n for n in path])
                return

            for i in range(index,len(s)):
                # check if its a valid number (0-255)
                if validNum(s[index:i+1]):
                    # PRUNE: CHECK IF THERE'S ENOUGH  OR TOO MANY CHARS
                    if len(s) - (i + 1) > (segmentsLeft - 1) * 3:
                        continue
                    if len(s) - (i + 1) < (segmentsLeft - 1): 
                        continue
                    
                    # ADD TO SOMETHING  
                    path.append(s[index:i+1])

                    # RECURSE
                    backtrack(i+1,segmentsLeft-1)

                    # UNDO
                    path.pop()

        backtrack(0,4)
        result = []

        return [".".join(a) for a in addresses]