class Solution:
    def solve(self,arr,start,ans):
        if start>=len(arr) or start<0:
            return False
        elif arr[start]==0:
        # ans[start]=True
            return True
        elif ans[start]==1:
            return False
        else:
            ans[start]=1
            return self.solve(arr, start+arr[start], ans) or self.solve(arr,start-arr[start],ans)


    def canReach(self, arr: List[int], start: int) -> bool:
        ans = [0] * len(arr)
        return self.solve(arr, start, ans)