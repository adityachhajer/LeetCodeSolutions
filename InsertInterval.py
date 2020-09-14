class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        i = 0
        n = len(intervals)
        while (i < n and intervals[i][1] < newInterval[0]):
            result.append(intervals[i])
            i += 1

        Mi = newInterval
        while (i < n and intervals[i][0] <= newInterval[1]):
            Mi[0] = min(intervals[i][0], Mi[0])
            Mi[1] = max(intervals[i][1], Mi[1])
            i += 1
        result.append(Mi)

        while i < n:
            result.append(intervals[i])
            i += 1
        return result