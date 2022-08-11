class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        length, width = len(grid), len(grid[0])
        islands = 0

        def dfs(row, col):
            if (row < 0 or row >= length or col < 0 or col >= width or
            grid[row][col] != "1"):
                return
            grid[row][col] = '#'
            
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)
            return
        
        for i in range(length):
            for j in range(width):
                if grid[i][j] == "1":
                    islands += 1
                    dfs(i, j)
                    
        return islands
