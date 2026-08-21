class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        max_area = 0
        
        def dfs(r,c):
            curr_max = 1
            if r not in range(rows) or c not in range(cols) or grid[r][c] == 0:
                return 0
            grid[r][c] = 0
            

            curr_max += dfs(r - 1, c)
            curr_max += dfs(r + 1, c)
            curr_max += dfs(r, c - 1)
            curr_max += dfs(r, c + 1)

            return curr_max

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    curr = dfs(r, c)
                    max_area = max(max_area, curr)

        return max_area
        



