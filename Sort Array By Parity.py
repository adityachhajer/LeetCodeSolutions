class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        ans=[]
        for i in A:
            if i%2==0:
                ans.insert(0,i)
            else:
                ans.append(i)
        return ans