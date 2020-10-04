class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        di={}
        for i in range(len(nums)):
            if nums[i] not in di.keys():
                di[nums[i]]=[i]
            else:
                di[nums[i]].append(i)
        c=0
        co=[]
        for i,j in enumerate(nums):
            # i=index
            # j=val
            x=j-k
            if x in di.keys():
                for t in di[x]:
                    if i!=t and [nums[i],nums[t]] not in co:
                        c=c+1
                        co.append([nums[i],nums[t]])
        return c


