class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # One pass binary search
        # Because the matrix is sorted row-wise and each row is sorted left-to-right, the entire matrix behaves like one big sorted array.
        # If we imagine flattening the matrix into a single list, the order of elements doesn't change.
        # This means we can run one binary search from index 0 to ROWS * COLS - 1.
        # This lets us access the correct matrix element without actually flattening the matrix.

        ROWS, COLS = len(matrix), len(matrix[0])

        l, r = 0, ROWS * COLS - 1
        while l <= r:
            # The below calc avoid overflow error
            # Overflow happens in other languages but not in python due to 2 reasons
            # *1. Dynamic handling of increasing integers
            # *2. No fixed size for numbers, they can grow to occupy entire memory
            # Thus, python never loops around a negative number
            m = l + (r - l) // 2

            # To get row and columns, you divide by the other's value since we multiplied them
            row, col = m // COLS, m % COLS

            # The row and col above are indices to find the exact value
            if target > matrix[row][col]:
                l = m + 1
            elif target < matrix[row][col]:
                r = m - 1
            else:
                return True
        return False