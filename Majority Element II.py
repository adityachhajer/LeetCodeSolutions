class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ans = []
        n = len(nums)
        n = n // 3
        di = {}
        for i in nums:
            if i in di.keys():
                di[i] += 1
            else:
                di[i] = 1
        for i, j in di.items():
            if j > n:
                ans.append(i)
        return ans
