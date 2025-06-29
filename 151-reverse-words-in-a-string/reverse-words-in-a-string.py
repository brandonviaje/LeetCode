class Solution:
    def reverseWords(self, s: str) -> str:
        
        """
        "the sky is blue"
                   ^
                  ^
        """
        build = []
        l,r = len(s) - 1, len(s) - 1

        while l >= 0:


            while l>=0 and s[l] == ' ':
                l -= 1
            r = l

            while l>= 0 and s[l] != ' ':
                l -= 1

            if r >= 0:
                build.append(s[l+1:r+1])

        return ' '.join(build)