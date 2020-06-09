class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort(reverse=True)
        while (len(stones) > 1):
            c = stones[0]
            d = stones[1]
            if c == d:
                stones.remove(c)
                stones.remove(d)
            if c != d:
                e = c - d
                stones.remove(c)
                stones.remove(d)
                stones.append(e)
                stones.sort(reverse=True)
        if len(stones) == 1:
            return stones[0]
        else:
            return 0

