class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i : i[0])
        trackerarr = [intervals[0]]

        for start, end in intervals[1:]:
            lastend = trackerarr[-1][1]

            if start <= lastend:
                trackerarr[-1][1] = max(lastend, end)
            else:
                trackerarr.append([start, end])

        return trackerarr
        