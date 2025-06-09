class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #sliding window
        seen = set()
        result = 0
        l = 0

        for r in range(len(s)):
            while s[r] in seen:
                #update sliding window
                seen.remove(s[l])
                l += 1 #shift pointer 

            seen.add(s[r]) #add current to our set
            result = max(result, r - l + 1) # update max

        return result
        