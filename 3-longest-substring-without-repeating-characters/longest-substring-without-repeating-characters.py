class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        result = 0
        left,right = 0,0
        seen = set()

        while right < len(s):

            # shrink window if we find a dupe
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            # add character to the seen set
            seen.add(s[right])
            result = max(result,right-left+1)
            right += 1

        return result
         