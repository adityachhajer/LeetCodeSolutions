class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        l=str.split(' ')
        di={}
        if len(pattern)!=len(l):
            return False
        else:
            for i in range(len(l)):
                if pattern[i] not in di.keys():
                    if l[i] not in di.values():
                        di[pattern[i]]=l[i]
                    else:
                        return False

                else:
                    x=di[pattern[i]]
                    if x!=l[i]:
                        return False

            return True
