"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        started = sorted([i.start for i in intervals])
        ended = sorted([i.end for i in intervals])

        res = count = 0
        s = e = 0

        for i in range(len(intervals)):
            if started[s] < ended[e]:
                s += 1
                count += 1
            else:
                e += 1
                count -= 1
            res = max(res, count)

        return res


            