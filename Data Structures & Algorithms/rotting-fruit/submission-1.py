from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time = 0
        fresh = 0 
        q = deque()
        rows , cols = len(grid), len(grid[0])
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                   q.append((i, j)) 
                elif grid[i][j] == 1:
                    fresh += 1


        while q and fresh > 0:
            level_length = len(q)
            directions = [(0,1), (0,-1), (1,0), (-1,0)]
            for _ in range(level_length):
                r, c = q.popleft()
                for dr, dc in directions: 
                    if 0 <= r + dr < rows and 0 <= c + dc < cols and grid[r + dr][c + dc] == 1:
                        grid[r + dr][c + dc] = 2
                        q.append((r + dr, c + dc))
                        fresh -= 1
            time += 1
        


        return time if fresh == 0 else -1 

                
"""
1. Keep track of fresh fruits
2. Find all rotten fruits (iterate through grid) and add them to queue
3. get length of queue to know what fruits to process
4. For each rotten fruit at each level rot their neighbours, add neighbours to queue
5. after each level increment time if there are still fresh fruits and rotten in the queue
6. if fresh after bfs left return -1 otherwise return time
"""


        

