class Solution:
    def __init__(self):
        self.pre=0
    def rand10(self):
        """
        :rtype: int
        """
        cur=(self.pre*7+rand7())%10+1
        self.pre=cur
        return cur