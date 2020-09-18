class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if(len(strs)==0):
            return ''
        ans=''
        for i in range(len(strs[0])):
            ans=strs[0][:i+1]
            for j in range(1,len(strs)):
                x=len(ans)
                p=strs[j][:x]
                if ans!=p:
                    return ans[:-1]
        return ans