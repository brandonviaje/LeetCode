class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = Counter(words)
        temp = [(-freq, word) for word, freq in counter.items()]

        # convert to max heap
        heapq.heapify(temp)

        result = []

        while k > 0:
            val = heapq.heappop(temp)
            result.append(val[1])
            k -= 1

        return result