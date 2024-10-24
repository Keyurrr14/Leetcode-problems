class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0] * n for _ in range(n)]
        left, right = 0, n - 1
        top, bottom = 0, n - 1
        val = 1

        while left <= right:
            # fill first row
            for c in range(left, right + 1):
                res[top][c] = val
                val += 1
            top += 1

            # fill right column
            for r in range(top, bottom + 1):
                res[r][right] = val
                val += 1
            right -= 1

            # fill bottom row (reverse order)
            for c in range(right, left - 1, -1):
                res[bottom][c] = val
                val += 1
            bottom -= 1

            # fill left column (reverse order)
            for r in range(bottom, top - 1, -1):
                res[r][left] = val
                val += 1
            left += 1

        return res
