class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten = []
        fresh = 0
        t = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    rotten.append([i, j])

        while len(rotten) > 0:
            num = len(rotten)
            for i in range(num):
                x, y = rotten[0]
                rotten.pop(0)
                if x > 0 and grid[x - 1][y] == 1:
                    grid[x - 1][y] = 2
                    fresh -= 1
                    rotten.append([x - 1, y])

                if y > 0 and grid[x][y - 1] == 1:
                    grid[x][y - 1] = 2
                    fresh -= 1
                    rotten.append([x, y - 1])

                if x < len(grid) - 1 and grid[x + 1][y] == 1:
                    grid[x + 1][y] = 2
                    fresh -= 1
                    rotten.append([x + 1, y])

                if y < len(grid[0]) - 1 and grid[x][y + 1] == 1:
                    grid[x][y + 1] = 2
                    fresh -= 1
                    rotten.append([x, y + 1])
            if len(rotten) > 0:
                t += 1
        return t if fresh == 0 else -1

