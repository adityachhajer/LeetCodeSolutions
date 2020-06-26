class Solution:
    def decodeString(self, s: str) -> str:
        if s=='':
            return ''
        l=[str(i) for i in range(0,10)]
        stack=[]
        for i in s:
            if i in l:
                stack.append(i)
            elif i=='[':
                stack.append('[')
            elif i==']':
                k=''
                while stack and stack[-1]!='[':
                    k=stack.pop()+k
                stack.pop()
                c=''
                while len(stack)!=0 and stack[-1] in l :
                    c=stack.pop()+c
                c=int(c)
                stack.append(c*k)
            else:
                stack.append(i)
        return ''.join(stack)