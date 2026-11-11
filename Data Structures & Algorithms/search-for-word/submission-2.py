class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # To optimize this, instead of storing a hash set of visited nodes,
        #   We can just update a visited node to a special symbol
        rows, cols = len(board), len(board[0])

        def backtrack(row, col, i):
            # Base case: all characters matched
            if i == len(word): return True

            # Invalid case: out of bounds, already visited, or character mismatch
            if (
                row < 0
                or row >= rows
                or col < 0
                or col >= cols
                or board[row][col] == '#'
                or board[row][col] != word[i]
            ):
                return False

            # Mark visited cell with a special symbol
            board[row][col] = '#'

            # Explore all 4 directions and save whether any path succeeds
            found = (
                backtrack(row + 1, col, i + 1)
                or backtrack(row, col + 1, i + 1)
                or backtrack(row - 1, col, i + 1)
                or backtrack(row, col - 1, i + 1)
            )

            
            # restore original character
            board[row][col] = word[i]

            return found

        # Try starting the word from every cell on the board
        for r in range(rows):
            for c in range(cols):
                if backtrack(r, c, 0):
                    return True

        return False
