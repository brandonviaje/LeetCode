class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        want to sort by start time

        compare the second interval with the very first, if the start time <= end time of the prev then we set the prev intervals end time to the max of the current end time and the prev
        else, we can just add the current start and end interval since it is not overlapping at all
        """

        intervals.sort(key = lambda i : i[0])
        result = [intervals[0]]

        for start,end in intervals[1:]:
            prev_end = result[-1][1]

            if start <= prev_end:
                result[-1][1] = max(prev_end,end)
            else:
                result.append([start,end])

        return result
