class Solution:
    def bitwiseComplement(self, N: int) -> int:
        x=bin(N)[2:]
        s=''
        for i in str(x):
            if i=='1':
                s=s+'0'
            else:
                s+='1'
        return int(s,2)