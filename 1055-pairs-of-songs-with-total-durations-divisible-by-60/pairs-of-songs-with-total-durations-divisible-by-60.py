class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        """
        we want to find the number of pairs of songs
        where their sum is divisble by 60.

        brute force: check each pair if their total duration is divisble by 60 and inc count

        optimal: similar to two sum, use hashmap to keep track of complement of mod, and also 
        add result the number  of times a song is divisible
        """
        result = 0
        remainders = defaultdict(int)

        for t in time:
            if t % 60 == 0:
                result += remainders[0]
            else:
                result += remainders[60-t%60]
         
            remainders[t % 60] += 1

        return result

        return result


        return result