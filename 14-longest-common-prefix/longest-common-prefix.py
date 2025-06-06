class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = min(strs)

        for i in range(len(strs)):
            word = strs[i]
            word = word[0:len(prefix)]

            for j in range(len(prefix)):
                if word[j] != prefix[j]:
                    prefix = prefix[:j]
                    break
                    
        if len(prefix) != 0:
            return prefix
        return ""
                