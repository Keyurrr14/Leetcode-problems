class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        if not matrix:
            return []
        
        zero_rows, zero_cols = set(), set()
        rows, cols = len(matrix), len(matrix[0])

        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    zero_rows.add(row)
                    zero_cols.add(col)

        for row in range(rows):
            for col in range(cols):
                if row in zero_rows or col in zero_cols:
                    matrix[row][col] = 0