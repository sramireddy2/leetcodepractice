from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        time, fresh = 0, 0

        ROWS, COLS = len(grid), len(grid[0])
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    queue.append([r, c])
       
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]        
        
        while queue and fresh > 0:
            # We increment time for each "level" of the BFS
            for i in range(len(queue)):
                r, c = queue.popleft()
                
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    
                    # 1. Check bounds
                    # 2. Check if the orange is actually fresh
                    if (row < 0 or row >= ROWS or 
                        col < 0 or col >= COLS or 
                        grid[row][col] != 1):
                        continue
                    
                    # Rot the orange and add to queue
                    grid[row][col] = 2
                    queue.append([row, col]) 
                    fresh -= 1
            
            time += 1
            
        return time if fresh == 0 else -1