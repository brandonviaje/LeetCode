class Solution:
    def reverseWords(self, s: str) -> str:
        def reverse_word(word):
            word = list(word)
            left, right = 0, len(word) - 1
            # two pointers to reverse
            while left < right:
                word[left], word[right] = word[right], word[left]
                left += 1
                right -= 1
            return ''.join(word)

        words = s.split(' ') # only parse the word not the spaces
        res = []

        # iterate through the list and reverse
        for word in words:
            res.append(reverse_word(word))

        return ' '.join(res)