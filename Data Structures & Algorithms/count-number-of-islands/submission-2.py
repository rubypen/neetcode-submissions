class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
        We want to count islands
        An island is composed of all of the 1s adjacent to it
        Adjacent here means to the left, right, up, and down of it

        Algorithm. Use bfs to explore the grid layer by layer.  
        when we are exploring an island, we mark the explored piece
        of land as 0 so we don't perform a repeat visit  


        An island portion is visited when we are visiting it
        The portion is explored when we have visited all its neighbors

        When we explore a new neighbor, we add it to the explore queueu
        When we finish exploring it goes to an explored list so we
        don't repeat.

        To count an island, we perform dfs when we find an index w. a 1
        '''
        count = 0
        queue = deque([])
        visited = set()

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def bfs(r, c):
            if (r, c) in visited:
                return

            if grid[r][c] == '0':
                return

            queue.append((r, c))
            visited.add((r, c))

            while queue:
                cr, cc = queue.popleft()

                for nr, nc in directions:
                    y, x = cr + nr, cc + nc
                    valid =  0 <= y < len(grid) and 0 <= x < len(grid[0])
                    if valid and grid[y][x] == '1' and (y, x) not in visited:
                        visited.add((y, x))
                        queue.append((y, x))

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1' and (r, c) not in visited:
                    bfs(r, c)
                    count += 1

        return count
