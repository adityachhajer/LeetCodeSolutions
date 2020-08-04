class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        ans=0
        l=arr[:k]
        x=sum(l)
        if x//k>=threshold:
            ans+=1
        for i in arr[k:]:
            x-=l.pop(0)
            x+=i
            l.append(i)
            if x//k>=threshold:
                ans+=1
        return ans