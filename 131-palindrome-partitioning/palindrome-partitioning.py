class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def isPalindrome(s):
            l,r = 0,len(s)-1
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1

            return True

        result = []

        def backtrack(index,path):
            # BASE CASE
            if index >= len(s): 
                result.append([s for s in path])
                return

            for i in range(index,len(s)):
                # CHECK IF SUBSTR IS PALINDROME
                if isPalindrome(s[index:i+1]):
                    # ADD TO SOMETHING
                    path.append(s[index:i+1])

                    # RECURSE
                    backtrack(i+1,path)
                    
                    # UNDO
                    path.pop()
                
        backtrack(0,[])
        return result