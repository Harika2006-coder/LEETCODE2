class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        def dfs(i,j):
            if i<0 or i>=m or j<0 or j>=n or grid[i][j]!=1:
                return 0
            else:
                grid[i][j]=0
                right= dfs(i,j+1) 
                down= dfs(i+1,j) 
                left= dfs(i,j-1) 
                up= dfs(i-1,j)

                return 1 + right + down + left + up
        max_area=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    num_islands=dfs(i,j)
                    max_area=max(max_area,num_islands)
              
        return max_area


        
