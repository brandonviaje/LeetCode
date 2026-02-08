class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        need to find the longest common prefix in all the strings
        LCP = ""

        [flower, flow, flight]
         ^
         ^

        LCP will be bottlecapped by the smallest string
        limit = min(limit,len(string)) 
        use the limit as the pointer, while ptr <= limit
        """

        if not strs:
            return LCP

        LCP = ""
        strs = sorted(strs) # sort the strings lexicographically

        # only need to worry about the first and last strings as they are the most alphabetically different
        first = strs[0]
        last = strs[-1]
        limit = len(min(first,last))

        for i in range(limit):
            # if no more common prefix return
            if(first[i] != last[i]):
                return LCP

            LCP += first[i]

        return LCP