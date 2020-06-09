class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = nums1 + nums2
        nums3.sort()
        if len(nums3) % 2 != 0:
            a = (len(nums3) - 1) // 2
            return nums3[a]
        else:
            a = len(nums3) // 2
            return (nums3[a] + nums3[a - 1]) / 2
