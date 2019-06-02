"""
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

For example,
Given [[0, 30],[5, 10],[15, 20]],
return 2.
"""


class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        sequence = []
        for interval in intervals:
            sequence.append((interval[0], 1))
            sequence.append((interval[1], 0))
        result = 0
        count = 0
        sorted_sequence = sorted(sequence, key=lambda x: (x[0], x[1]))
        for each in sorted_sequence:
            if each[1] == 1:
                count += 1
            else:
                count -= 1
            result = max(result, count)
        return result


def meetingRooms(schedule):
    sequence = []
    for i in range(len(schedule)):
        sequence.append((schedule[i][0], 'start'))
        sequence.append((schedule[i][1], 'end'))

    sequence.sort()
    count = 0
    result = 0
    for i in range(len(sequence)):
        if sequence[i][1] == 'start':
            count += 1
        else:
            count -= 1
        result = max(result, count)
    return result


schedule = [[0, 30],[5, 10],[15, 20]]
print(meetingRooms(schedule))
