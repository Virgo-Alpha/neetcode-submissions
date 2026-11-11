class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def backtrack(row, col, visited, i):
            # Base case: all characters matched
            if i == len(word): return True

            # Invalid case: out of bounds, already visited, or character mismatch
            if (
                row < 0
                or row >= rows
                or col < 0
                or col >= cols
                or (row, col) in visited
                or board[row][col] != word[i]
            ):
                return False

            # Mark current cell as visited
            visited.add((row, col))

            # Explore all 4 directions and save whether any path succeeds
            found = (
                backtrack(row + 1, col, visited, i + 1)
                or backtrack(row, col + 1, visited, i + 1)
                or backtrack(row - 1, col, visited, i + 1)
                or backtrack(row, col - 1, visited, i + 1)
            )

            # Backtrack: unmark current cell
            visited.remove((row, col))

            return found

        # Try starting the word from every cell on the board
        for r in range(rows):
            for c in range(cols):
                if backtrack(r, c, set(), 0):
                    return True

        return False
