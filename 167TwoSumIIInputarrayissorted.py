class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        di = {}
        for i in range(0, len(numbers)):
            di[numbers[i]] = i + 1
        for j in range(0, len(numbers)):
            d = target - numbers[j]
            if d in di.keys():
                return [j + 1, di[d]]
