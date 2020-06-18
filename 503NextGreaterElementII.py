class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        l = []
        for i in range(len(nums)):
            k = nums[i + 1:] + nums[:i]
            for j in k:
                if j > nums[i]:
                    l.append(j)
                    break
            if len(l) == i + 1:
                continue
            else:
                l.append(-1)
        return l
