class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        di = {}
        for i in range(0, len(nums)):
            di[nums[i]] = i
        for i in range(0, len(nums) - 1):
            a = target - nums[i]
            if a in di.keys():
                if (i != di[a]):
                    return [i, di[a]]




