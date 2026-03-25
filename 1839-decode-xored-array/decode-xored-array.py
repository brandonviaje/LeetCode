class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        arr = [0] * (len(encoded) + 1)
        arr[0] = first

        # decode XOR
        for i in range(len(encoded)):
            arr[i+1] = arr[i] ^ encoded[i]

        return arr