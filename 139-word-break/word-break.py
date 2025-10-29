class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        Subproblem: check if the substrings of s are in the wordDict
        once you find a substring s[start:end] in wordDict, the next overlapping subproblem would be at the starting index of end +1
        """
        # makes it O(1) lookups
        wordDict = set(wordDict)
        memo = {}

        def DP(start):
            # check memo table
            if start in memo:
                return memo[start]

            # base case, if we reach the len of s then we have found a valid substring
            if start == len(s):
                return True

            for end in range(start+1,len(s)+1):
                # if you find a substring thats in word dict, check the next substring of s to see if its in wordDict also
                if s[start:end] in wordDict and DP(end):
                    memo[start] = True # store it as true 
                    return True # return True after

            # couldn't find any or anymore of a substring in wordDict
            memo[start] = False
            return False


        return DP(0)