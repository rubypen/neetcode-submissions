class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # Game Plan: perform the same algorithm as per the previous quesition, but
        # tweak bfs to return the count of island area; then when returned, 
        # append to a list and once the list is populated, find the max

        rows, cols = len(grid), len(grid[0])
        islandAreas = []
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(r, c):
            q = deque()
            grid[r][c] = 0
            q.append((r, c))
            area = 0

            while q: 
                r, c = q.popleft()
                for dx, dy in dirs:
                    x, y = c + dx, r + dy
                    valid_coord = x >= 0 and x < cols and y >= 0 and y < rows
                    if valid_coord and grid[y][x] == 1:
                        grid[y][x] = 0 # updating as visited
                        q.append((y, x))
                        area += 1
            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    area = 1 + bfs(r, c)
                    islandAreas.append(area)
        return max(islandAreas, default = 0)


                
        