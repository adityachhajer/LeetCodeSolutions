class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        num='123456789'
        a=len(str(low))
        b=len(str(high))
        ans=[]
        for i in range(a,b+1):
            for j in range(9-i+1):
                x=int(num[j:i+j])
                if low<=x<=high:
                    ans.append(x)
        return ans