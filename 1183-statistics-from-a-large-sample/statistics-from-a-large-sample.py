class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        """
        build the sample
        """
        min_val = float('inf')
        max_val = float('-inf')
        mode = 0
        mean = 0
        median = 0
        mode_freq = 0
        sample_len = 0
        n = sum(count)

        for key, freq in enumerate(count):
            # skip if num doesn't appear in sample
            if freq == 0:
                continue

            # get min and max val in sample
            min_val = min(min_val, key)
            max_val = max(max_val, key)

            # update mean
            mean += key * freq
            sample_len += freq

            # update mode
            if mode_freq < freq:
                mode = key
                mode_freq = freq

        # calculate mean
        mean = mean / sample_len

        # calculate median
        for i in range(255):
            count[i+1] += count[i]
            median1 = bisect.bisect(count, (n-1) / 2)
            median2 = bisect.bisect(count, n/2)
            median = (median1 + median2) / 2

        return [min_val, max_val, mean, median, mode]