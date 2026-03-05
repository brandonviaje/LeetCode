class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        """
        a person can attend a meeting if the start of a meeting does not interfere with any other meeting intervals
        that means that the start time can not be in between the end interval of another meeting. they must all be different

        to do this efficiently, we can sort the array by start times from earliest time to latest start time. then we check if 
        the current meeting is <= end of the prev meeting. if it is, then you can not attend all meetings.

        return true at the end which means none of the times conflict with each other
        """

        intervals.sort()
        print(intervals)

        for i in range(1,len(intervals)):
            if intervals[i][0] < intervals[i-1][1]:
                return False

        return True