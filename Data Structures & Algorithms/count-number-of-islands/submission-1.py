from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        # Renamed to ROWS/COLS to avoid shadowing issues
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def bfs(r, c):
            queue = deque()
            visited.add((r, c))
            queue.append((r, c))

            while queue:
                # Use curr_r/curr_c to leave ROWS/COLS untouched
                curr_r, curr_c = queue.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    nr, nc = curr_r + dr, curr_c + dc
                    
                    # 1. Bound check using the constant ROWS/COLS
                    # 2. Check if it is land ('1')
                    # 3. Check if we've been there
                    if (nr in range(ROWS) and nc in range(COLS) 
                        and grid[nr][nc] == "1" and (nr, nc) not in visited):
                        queue.append((nr, nc)) # Fixed naming
                        visited.add((nr, nc))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1
                    
        return islands