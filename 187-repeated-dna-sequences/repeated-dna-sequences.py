class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        subStr = list()
        seen = set()
        result = set()

        if len(s) < 10:
            return []

        r = 0

        # get all the 10 character subStrs using sliding window
        while r < len(s):

            subStr.append(s[r])
            r += 1
            # once subStr is 10, check if it is already seen then add to result
            if len(subStr) == 10:
                if "".join(subStr) in seen:
                    result.add("".join(subStr))
                else:
                    seen.add("".join(subStr))

                del subStr[0] #update window

        return list(result)

        # T O(n) S O(n)