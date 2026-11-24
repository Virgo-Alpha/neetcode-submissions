class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # An island is a group of connected 1s.
        # To find the maximum area, we explore each island fully and count how many cells it contains.

        ROWS, COLS = len(grid), len(grid[0])
        visit = set()

        def dfs(r, c):
            """
            dfs helps us:
            - Start from a land cell
            - Visit all connected land cells (up, down, left, right)
            - Count the size of that island
            - Keep track of the largest size seen
            """
            if (r < 0 or r == ROWS or c < 0 or
                c == COLS or grid[r][c] == 0 or
                (r, c) in visit
            ):
                return 0
            visit.add((r, c))
            return (1 + dfs(r + 1, c) +
                        dfs(r - 1, c) +
                        dfs(r, c + 1) +
                        dfs(r, c - 1))

        area = 0
        for r in range(ROWS):
            for c in range(COLS):
                area = max(area, dfs(r, c))
        return area