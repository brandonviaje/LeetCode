class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        seen = set()

        freq_map = Counter(arr)

        for num,freq in freq_map.items():
            if freq in seen:
                return False

            seen.add(freq)

        return True