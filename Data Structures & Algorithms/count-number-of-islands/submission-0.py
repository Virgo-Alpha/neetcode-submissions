class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        We can use the Depth First Search (DFS) algorithm to traverse 
            each group independently. 
        We iterate through each cell of the grid.
        When we encounter a 1, we perform a DFS starting at that cell and 
            recursively visit every other 1 that is reachable. 
        During this process, we mark the visited 1's as 0 to 
            ensure we don't revisit them, as they belong to the same group. 
        The number of groups corresponds to the number of islands.
        """
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0

        def dfs(r, c):
            if (r < 0 or c < 0 or r >= ROWS or
                c >= COLS or grid[r][c] == "0"
            ):
                return

            grid[r][c] = "0"
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    dfs(r, c)
                    islands += 1

        return islands
