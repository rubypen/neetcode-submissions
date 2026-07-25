from collections import deque
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Game Plan: 
        # dirs = generalize directions in which to search for island portion
        # islandCount = to update num of islands; mark islands as 0 when visited
        # use bfs to search what "nodes" are connected to eachother to create an
        # island; once bfs is done that means we have finished exploring an island;
        # update island count until final answer is acquired

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        islandCount = 0
        rows, cols = len(grid), len(grid[0])

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            grid[r][c] = "0"

            while q: # while there are still entries in the queue
                r, c = q.popleft()
                for y, x in dirs:
                    dy, dx = r + y, c + x
                    if dy >= 0 and dy < rows and dx >= 0 and dx < cols and grid[dy][dx] == "1":
                        grid[dy][dx] = "0"
                        q.append((dy, dx)) # my issue was that i didn't ensure valid bounds

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    bfs(r, c)
                    islandCount += 1

        return islandCount 

