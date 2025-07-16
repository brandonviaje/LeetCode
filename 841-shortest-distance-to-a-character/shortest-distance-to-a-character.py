class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        """
        do a for loop, and make answer arr

        if s[i] != c, then shift pointer until u hit a c


        loveleetcode
         ^
           ^
        """
        answer = [0] * len(s)
        seen = []
        prev = float('inf')
        res = 0

        for i in range(len(s)):
            if s[i] == c:
                seen.append(i)

        for i in range(len(s)):
            if s[i] != c:
                
                # determine the closest index
                for index in seen:
                    if abs(i-index) < prev:
                        prev = abs(i-index)
                        res = index

                answer[i] = abs(i-res)
                prev = float('inf') # reset prev

        return answer


