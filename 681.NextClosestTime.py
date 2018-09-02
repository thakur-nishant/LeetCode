"""
Given a time represented in the format "HH:MM", form the next closest time by reusing the current digits. There is no limit on how many times a digit can be reused.

You may assume the given input string is always valid. For example, "01:34", "12:09" are all valid. "1:34", "12:9" are all invalid.

Example 1:

Input: "19:34"
Output: "19:39"
Explanation: The next closest time choosing from digits 1, 9, 3, 4, is 19:39, which occurs 5 minutes later.  It is not 19:33, because this occurs 23 hours and 59 minutes later.
Example 2:

Input: "23:59"
Output: "22:22"
Explanation: The next closest time choosing from digits 2, 3, 5, 9, is 22:22. It may be assumed that the returned time is next day's time since it is smaller than the input time numerically.

"""


class Solution:
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        hrs, mins = time.split(":")
        get_nums = list(time)
        get_nums.remove(":")
        get_nums = sorted(set(get_nums))
        get_nums = [int(i) for i in get_nums]
        # print(get_nums)
        poss_hrs, poss_mins = self.getPermutation(get_nums)

        # print(poss_hrs, poss_mins)
        if poss_mins.index(int(mins)) == len(poss_mins) - 1:
            if poss_hrs.index(int(hrs)) == len(poss_hrs) - 1:
                return '{0:02d}'.format(poss_hrs[0]) + ":" + '{0:02d}'.format(poss_mins[0])
            else:
                return '{0:02d}'.format(poss_hrs[poss_hrs.index(int(hrs)) + 1]) + ":" + '{0:02d}'.format(poss_mins[0])
        else:
            return '{0:02d}'.format(int(hrs)) + ":" + '{0:02d}'.format(poss_mins[poss_mins.index(int(mins)) + 1])

    def getPermutation(self, num):
        possible_hrs = []
        possible_mins = []
        for i in num:
            for j in num:
                temp = i * 10 + j
                if temp < 24:
                    possible_hrs.append(temp)
                if temp < 60:
                    possible_mins.append(temp)

        return possible_hrs, possible_mins



