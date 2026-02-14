class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        """
        a person cannot attend a meeting if one of the intervals[i][0] is < intervals[i-1][1]
        sort the array by starting times to make it easier to track and return false
        """
        intervals.sort()

        if len(intervals) <= 1:
            return True
        
        # check if any conflicting meeting intervals
        for i in range(1,len(intervals)):
            if intervals[i][0] < intervals[i-1][1]:
                return False

        print(intervals)

        return True