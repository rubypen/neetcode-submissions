from collections import deque
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        row_len, col_len = len(grid), len(grid[0])
        count = 0

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            grid[r][c] = "0"

            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    newrow, newcol = r + dr, c + dc
                    if (newrow < 0 or newrow >= row_len or
                        newcol < 0 or newcol >= col_len or
                        grid[newrow][newcol] == "0"):
                        continue
                    q.append((newrow, newcol))
                    grid[newrow][newcol] = "0"

        for r in range(row_len):
            for c in range(col_len):
                if grid[r][c] == "1":
                    bfs(r, c)
                    count += 1

        return count
