class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
       rows, cols = len(grid), len(grid[0])
       islands = 0
    
       def dfs(grid, i , j):
           if not rows > i >= 0 or not cols > j >= 0 or grid[i][j] == "0":
              return   
           grid[i][j] = "0" 
           dfs(grid, i - 1,j)
           dfs(grid,i + 1,j)
           dfs(grid, i, j - 1)            
           dfs(grid, i, j + 1)
           
       for i in range(0, rows):
            for j in range(0, cols):
                if grid[i][j] == "1":
                    islands += 1 
                    dfs(grid, i, j)

       return islands
