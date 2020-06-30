class Solution:
    def solve(self,candidates,target,i,k,l):
        if target==0:
            l.append(k)
            return 1
        elif i==0:
            return 0
        else:
            if candidates[i-1]>target:
                return self.solve(candidates,target,i-1,k,l)
            else:
                return self.solve(candidates,target-candidates[i-1],i,[candidates[i-1]]+k,l)+self.solve(candidates,target,i-1,k,l)
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        l=[]
        self.solve(candidates,target,len(candidates),[],l)
        return l