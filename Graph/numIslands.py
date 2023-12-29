# 200) Number of islands

class Solution:
    def numIslands(self, grid):
        # grid: List[List[str]]
        # rtype: int
        
        # bfs / dfs - ok
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])

        visited = set()
        islands = 0
        directions = [[1, 0], [-1,0], [0, 1], [0, -1]]

        def dfs(r, c):
            visited.add((r, c))

            for dx, dy in directions:
                next_r, next_c = r + dx, c + dy
                if (next_r in range(rows) and next_c in range(cols) and grid[next_r][next_c] == "1" and (next_r, next_c) not in visited):
                    dfs(next_r, next_c)
    

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    dfs(r, c)
                    islands += 1
        
        return islands

        
