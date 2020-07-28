class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:

        zeros, lakes, res = [], {}, [-1] * len(rains)
        for i, val in enumerate(rains):
            if val in lakes:
                idx = bisect.bisect_left(zeros, lakes[val])
                if idx == len(zeros): return []
                res[zeros[idx]] = val
                zeros.pop(idx)
                lakes[val] = i
            elif val == 0:
                zeros.append(i)
            else:
                lakes[val] = i
        for i in range(len(res)):
            if rains[i] == 0 and res[i] == -1:
                res[i] = 1
        return res