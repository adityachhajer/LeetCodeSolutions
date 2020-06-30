from queue import PriorityQueue
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        q = PriorityQueue()
        for i in nums:
            q.put(i)

        k = len(nums) - k + 1
        c = 0
        while not q.empty():
            c = c + 1
            ni = q.get()
            if c == k:
                return ni
