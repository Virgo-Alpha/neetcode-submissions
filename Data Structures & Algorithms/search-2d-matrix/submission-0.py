class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # // flatten it
        # use binary search - because the matrix is sorted
        # We can use binary search twice, first on the overall matrix then on target row

        # The target, if present, will be in a single row

        # Binary search on the rows
        rows = [row[0] for row in matrix]
        l, r = 0, len(rows) - 1

        while l <= r:
            middle = (l + r) // 2

            
            if rows[middle] == target:
                return True
            elif rows[middle] > target:
                r = middle - 1
            elif rows[middle] < target:
                l = middle + 1

        # We need to identify the target row so as to perform the second binary search
        # When the loop exits without returning True:
        # If the target is not found exactly, l overshoots and points to a row whose values are strictly greater than the target
        # If the target is greater than every single element in the entire matrix, l will increment until it equals len(matrix)
        # r is also the idx of the row in the matrix so the target row is:
        target_row = matrix[r]

        # second binary search
        l, r = 0, len(target_row) - 1

        while l <= r:
            middle = (l + r) // 2

            
            if target_row[middle] == target:
                return True
            elif target_row[middle] > target:
                r = middle - 1
            elif target_row[middle] < target:
                l = middle + 1

        return False
