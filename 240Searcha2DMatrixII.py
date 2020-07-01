class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix==[[]]:
            return False
        for i in matrix:
            if i[0]==target or i[-1]==target:
                return True
            elif target>i[0] and target<i[-1]:
                start=0
                end=len(i)-1
                while start<=end:
                    mid=start+(end-start)//2
                    if i[mid]==target:
                        return True
                    elif i[mid]<target:
                        start=mid+1
                    else:
                        end=mid-1
        return False