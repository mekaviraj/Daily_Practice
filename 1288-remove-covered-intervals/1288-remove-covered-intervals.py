class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))

        ans = len(intervals)
        removed = [False] * len(intervals)

        for i in range(len(intervals)):
            if removed[i]:
                continue
            for j in range(i + 1, len(intervals)):
                if intervals[i][0] <= intervals[j][0] and intervals[i][1] >= intervals[j][1]:
                    if not removed[j]:
                        removed[j] = True
                        ans -= 1

        return ans