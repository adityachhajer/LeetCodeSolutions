class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        l=[]
        for i in range(len(nums)):
            if nums[i]==1:
                if len(l)==0:
                    l.append(i)
                else:
                    if i-l[-1]<=k:
                        return False
                    l.append(i)
        return True