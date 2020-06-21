class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr1 = sorted(arr1)
        ans = []
        for i in arr2:
            x = arr1.count(i)
            ans += [i] * x
            for j in range(x):
                arr1.remove(i)
        return ans + arr1


