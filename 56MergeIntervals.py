class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if intervals == []:
            return []
        intervals.sort()
        stack = []
        stack.append(intervals[0])
        for i in range(1, len(intervals)):
            if intervals[i][0] > stack[-1][1]:
                stack.append(intervals[i])
            else:
                if intervals[i][0] >= stack[-1][0]:
                    if intervals[i][1] <= stack[-1][1]:
                        continue
                    else:
                        stack[-1][1] = intervals[i][1]
        return stack
