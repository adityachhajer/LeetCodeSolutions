class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num==1 or num==4:
            return True
        if num==0:
            return False
        while num%4==0:
            num=num//4
            if num ==4 :
                return True
        return False