class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = sum(nums[:3])
        for i in range(len(nums) - 2):
            s = i + 1
            e = len(nums) - 1
            while (s < e):
                sumuptohere = nums[i] + nums[s] + nums[e]
                if abs(sumuptohere - target) < abs(res - target):
                    res = sumuptohere
                if sumuptohere < target:
                    s = s + 1
                else:
                    e -= 1
        return res
