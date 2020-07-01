class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        while(start<=end):
            mid = (start+end)//2
            if(nums[mid] == target):
                return mid
            elif(target < nums[mid]):
                if(target < nums[start] and nums[start] <= nums[mid]):
                    start = mid + 1
                else:
                    end = mid - 1
            elif(target > nums[mid]):
                if(target > nums[end] and nums[end] > nums[mid]):
                    end = mid - 1
                else:
                    start = mid + 1
        return -1