class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l = []
        for i in range(len(nums1)):
            x = nums2.index(nums1[i])
            for j in range(x, len(nums2)):
                if nums2[j] > nums1[i]:
                    l.append(nums2[j])
                    break
            if len(l) == i + 1:
                continue
            else:
                l.append(-1)
        return l
