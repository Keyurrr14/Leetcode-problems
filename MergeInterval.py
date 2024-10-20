class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort(key=lambda x: x[0])

        previous = intervals[0]
        for interval in intervals[1:]:
            if interval[0] <= previous[1]:
                previous[1] = max(previous[1], interval[1])
            else:
                res.append(previous)
                previous = interval

        res.append(previous)
        return res