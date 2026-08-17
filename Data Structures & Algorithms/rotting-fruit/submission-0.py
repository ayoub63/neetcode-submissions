from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        def bfs(grid):
            fresh = 0
            time = 0
            q = deque()
            
            for i in range(ROWS):
                for j in range(COLS):
                    if grid[i][j] == 2:
                        q.append((i, j))
                    if grid[i][j] == 1:
                        fresh += 1
            while q and fresh > 0:
                time_interval = len(q)
                directions = [(0, 1),(0, - 1),(1, 0),(-1, 0)]
                for _ in range(time_interval):
                    r, c = q.popleft()
                    for dr, dc in directions:
                        if 0 <= r + dr < ROWS and 0 <= c + dc < COLS and grid[r + dr][c + dc] == 1:
                            grid[r + dr][c + dc] = 2
                            q.append((r + dr, c + dc))
                            fresh -= 1
                time += 1        
            if fresh == 0:
                return time
            if fresh > 0: 
                return -1          
                
            return time

        return bfs(grid)
     
        








"""
find and add starting fruit to queue
add to visited
pop rotten fruit, rotten its neighbours if 1
add neighbours to queue
time += 1
pop and do the same again

"""