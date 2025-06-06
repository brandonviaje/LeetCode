class Solution:
    def romanToInt(self, s: str) -> int:
        map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        sum = 0
        i = 0

        while i < len(s):
            curr = map[s[i]]
            if i + 1 < len(s):
                next = map[s[i + 1]]
                if curr < next:
                    sum += next - curr
                    i += 2  # Skip both characters
                    continue
            sum += curr
            i += 1

        return sum
