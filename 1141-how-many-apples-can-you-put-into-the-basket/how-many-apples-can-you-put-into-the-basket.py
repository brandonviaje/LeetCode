class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        """
        what we can do is check if adding this apple exceeds the limit

        if it doesn't then we can update our length by doing max(result, (i - l) + 1)

        brute force:
        try all combinations of weight and then get length from j-i

        we can sort the array, and make a prefix sum arr
        then as long as prefix[i] <= 5000, update a result variable max(result,i+1)
        """

        weight.sort()
        prefix = [0] * len(weight)
        prefix[0] = weight[0]

        for i in range(1,len(weight)):
            prefix[i] = prefix[i-1] + weight[i]

        result = float('-inf')
        print(prefix)

        for i in range(len(prefix)):
            if prefix[i] <= 5000:
                result = max(result, i+1)

        return result