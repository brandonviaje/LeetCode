class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramStr = defaultdict(list)

        for s in strs:
            # create array to count how many letters are in each string
            arr = [0] * 26
            for c in s:
                # map the character from 0 to 25
                arr[ord(c) - ord('a')] += 1

            # convert array to tuple so u can use it in map
            key = tuple(arr)
            anagramStr[key].append(s) # add word if the same char arr

        return list(anagramStr.values())        

        # T O(n * k) S O(n * k)