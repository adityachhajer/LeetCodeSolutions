class Solution:
    def addBinary(self, a: str, b: str) -> str:
        s1 = int(a, 2)
        s2 = int(b, 2)
        s3 = int(s1) + int(s2)
        s4 = bin(s3).replace("0b", "")
        return str(s4)

