class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        need to group anagrams together
        
        we can group all anagrams that have the same amount of characters together using a hashmap
        if the curr str has same character count with another, add it to that bucket
        """

        result = defaultdict(list)

        for s in strs:
            arr = [0] * 26
            for char in s:
                arr[ord(char) - ord('a')] += 1 # add how many times letter is present

            result[tuple(arr)].append(s) # add to strings with same freq arrr

        return list(result.values())
            