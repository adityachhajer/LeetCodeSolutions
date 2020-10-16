class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0 or k == 0:
            return nums
        a = list(nums)
        k = k % len(nums)
        while k > 0:
            a = a[-1:-2:-1] + a[:-1]
            k -= 1
        for i in range(len(a)):
            nums[i] = a[i]

